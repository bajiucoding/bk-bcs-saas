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


def get_cluster_tasks_mod():
    try:
        from backend.apps.cluster.flow_views_ext import tasks
    except ImportError:
        from backend.apps.cluster.flow_views import tasks
    return tasks


def get_cluster_mod():
    try:
        from backend.apps.cluster.flow_views_ext import cluster
    except ImportError:
        from backend.apps.cluster.flow_views import cluster
    return cluster


def get_cluster_node_mod():
    try:
        from backend.apps.cluster.flow_views_ext import node
    except ImportError:
        from backend.apps.cluster.flow_views import node
    return node


def get_cmdb_mod():
    try:
        from backend.apps.cluster.flow_views_ext.tools import cmdb
    except ImportError:
        from backend.apps.cluster.flow_views.tools import cmdb
    return cmdb


def get_gse_mod():
    try:
        from backend.apps.cluster.flow_views_ext.tools import gse
    except ImportError:
        from backend.apps.cluster.flow_views.tools import gse
    return gse


def get_cluster_node_task_mod():
    try:
        from backend.apps.cluster.flow_views_ext import tasks as cluster_node_tasks
    except ImportError:
        from backend.apps.cluster.flow_views import tasks as cluster_node_tasks
    return cluster_node_tasks