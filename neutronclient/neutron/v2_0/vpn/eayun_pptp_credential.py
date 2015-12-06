# Copyright (c) 2015 Eayun, Inc.
# All rights reserved.
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

from neutronclient.neutron import v2_0 as neutronv20
from neutronclient.openstack.common.gettextutils import _


class ListPPTPCredential(neutronv20.ListCommand):
    """List PPTP credentials that belong to a given tenant."""

    resource = 'pptp_credential'
    list_columns = ['id', 'username', 'password', 'vpnservices']
    pagination_support = True
    sorting_support = True


class ShowPPTPCredential(neutronv20.ShowCommand):
    """Show information of a given PPTP credential."""

    resource = 'pptp_credential'


class CreatePPTPCredential(neutronv20.CreateCommand):
    """Create an PPTP credential."""

    resource = 'pptp_credential'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'username', metavar='USERNAME',
            help=_('Username of the PPTP credential.'))
        parser.add_argument(
            'password', metavar='PASSWORD',
            help=_('Password of the PPTP credential.'))

    def args2body(self, parsed_args):
        body = {
            'pptp_credential': {
                'username': parsed_args.username,
                'password': parsed_args.password,
            }
        }
        return body


class UpdatePPTPCredential(neutronv20.UpdateCommand):
    """Update a given PPTP credential."""

    resource = 'pptp_credential'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--password', help=_('Updated password of the PPTP credential.'))

    def args2body(self, parsed_args):
        body = {'pptp_credential': {}}
        if parsed_args.password:
            body['pptp_credential'].update({'password': parsed_args.password})
        return body


class DeletePPTPCredential(neutronv20.DeleteCommand):
    """Delete a given PPTP credential."""

    resource = 'pptp_credential'
