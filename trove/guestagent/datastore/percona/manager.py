# Copyright 2015 Tesora, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from oslo_utils import importutils
from trove.guestagent.datastore.mysql_common import manager


MYSQL_APP = ("trove.guestagent.datastore.percona.service."
             "MySqlApp")
MYSQL_APP_STATUS = ("trove.guestagent.datastore.percona.service."
                    "MySqlAppStatus")
MYSQL_ADMIN = ("trove.guestagent.datastore.percona.service."
               "MySqlAdmin")


class Manager(manager.MySqlManager):

    def __init__(self):
        mysql_app = importutils.import_class(MYSQL_APP)
        mysql_app_status = importutils.import_class(MYSQL_APP_STATUS)
        mysql_admin = importutils.import_class(MYSQL_ADMIN)

        super(Manager, self).__init__(mysql_app, mysql_app_status, mysql_admin)
