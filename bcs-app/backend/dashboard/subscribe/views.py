# -*- coding: utf-8 -*-
#
# Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
# Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
from django.utils.translation import ugettext_lazy as _
from kubernetes.client import ApiException
from rest_framework.response import Response

from backend.bcs_web.viewsets import SystemViewSet
from backend.dashboard.exceptions import ResourceVersionExpired
from backend.dashboard.subscribe.constants import (
    DEFAULT_SUBSCRIBE_TIMEOUT,
    K8S_API_GONE_STATUS_CODE,
    KIND_RESOURCE_CLIENT_MAP,
)
from backend.dashboard.subscribe.serializers import FetchResourceWatchResultSLZ
from backend.resources.constants import K8sResourceKind
from backend.resources.custom_object import CustomObject
from backend.utils.basic import getitems


class SubscribeViewSet(SystemViewSet):
    """ 订阅相关接口，检查 K8S 资源变更情况 """

    def list(self, request, project_id, cluster_id):
        """获取指定资源某resource_version后变更记录"""
        params = self.params_validate(FetchResourceWatchResultSLZ)

        if params['kind'] in KIND_RESOURCE_CLIENT_MAP:
            # 根据 Kind 获取对应的 K8S Resource Client 并初始化
            Client = KIND_RESOURCE_CLIENT_MAP[params['kind']]
            resource_client = Client(request.ctx_cluster)
        else:
            # 自定义资源类型走特殊的获取 ResourceClient 逻辑
            resource_client = CustomObject(request.ctx_cluster, kind=params['kind'], api_version=params['api_version'])
        res_version = params['resource_version']
        try:
            events = resource_client.watch(resource_version=res_version, timeout=DEFAULT_SUBSCRIBE_TIMEOUT)
        except ApiException as e:
            if e.status == K8S_API_GONE_STATUS_CODE:
                raise ResourceVersionExpired(_('ResourceVersion {} 已过期，请重新获取').format(res_version))
            raise

        # events 默认按时间排序，取最后一个 ResourceVersion 即为最新值
        latest_rv = getitems(events[-1], 'manifest.metadata.resourceVersion') if events else None
        response_data = {'events': events, 'latest_rv': latest_rv}
        return Response(response_data)
