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
import json
import logging

from kubernetes import client

from backend.resources.constants import K8sResourceKind

from .api_response import response
from .resource import APPAPIClassMixins, FilterResourceData, Resource

logger = logging.getLogger(__name__)


class Deployment(Resource, FilterResourceData, APPAPIClassMixins):
    resource_kind = K8sResourceKind.Deployment.value

    @response()
    def create_deployment(self, namespace, data):
        return self.api_instance.create_namespaced_deployment(namespace, data)

    @response()
    def delete_deployment(self, namespace, name):
        body = client.V1DeleteOptions()
        resp = self.api_instance.delete_namespaced_deployment(name, namespace, body=body)
        return resp

    @response(format_data=False)
    def get_deployment(self, params):
        # 因为view层向下传递时是多个namespace+name, 需要增加过滤
        resp = self.api_instance.list_deployment_for_all_namespaces(_preload_content=False)
        data = json.loads(resp.data)
        return self.filter_data(self.resource_kind, data, params)

    @response()
    def update_deployment(self, namespace, name, data):
        return self.api_instance.replace_namespaced_deployment(name, namespace, data)

    @response()
    def patch_deployment(self, namespace, name, data):
        return self.api_instance.patch_namespaced_deployment(name, namespace, data)
