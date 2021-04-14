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
from backend.apis.views import NoAccessTokenBaseAPIViewSet
from backend.dashboard.custom_object.views import CustomObjectViewSet


class CustomObjectAPIViewSet(NoAccessTokenBaseAPIViewSet, CustomObjectViewSet):
    def patch_custom_object(self, request, project_id_or_code, cluster_id, crd_name, name):
        return super(CustomObjectAPIViewSet, self).patch_custom_object(
            request, request.project.project_id, cluster_id, crd_name, name
        )