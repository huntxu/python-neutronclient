# Copyright 2017 Eayun Inc.
# All Rights Reserved
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
#


from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListL7policy(neutronV20.ListCommand):
    """List L7policies that belong to a given tenant."""

    resource = 'l7policy'
    list_columns = ['id', 'name', 'pool_id', 'priority',
                    'action', 'key', 'value',
                    'admin_state_up', 'status']
    pagination_support = True
    sorting_support = True


class ShowL7policy(neutronV20.ShowCommand):
    """Show information of a given l7policy."""

    resource = 'l7policy'


class CreateL7policy(neutronV20.CreateCommand):
    """Create a l7policy."""

    resource = 'l7policy'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            help=_('Set admin state up to false.'))
        parser.add_argument(
            '--priority',
            required=True,
            help=_('The priority(valid in [0,255]) for l7policy'))
        parser.add_argument(
            '--pool-id', metavar='POOL',
            default=None,
            help=_('The l7policy of pool that belong.'))
        parser.add_argument(
            '--action',
            required=True,
            choices=['block', 'redirect', 'addHeader'],
            help=_('Exec action on the l7policy if l7rule match.'))
        parser.add_argument(
            '--key',
            help=_('The key of the l7policy action keyword.'))
        parser.add_argument(
            '--value',
            help=_('The value of the l7policy action values.'))

    def args2body(self, parsed_args):
        _pool_id = None
        if parsed_args.pool_id:
            _pool_id = neutronV20.find_resourceid_by_name_or_id(
                self.get_client(), 'pool', parsed_args.pool_id)
        body = {
            self.resource: {
                'admin_state_up': parsed_args.admin_state,
                'pool_id': _pool_id,
            },
        }
        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['priority', 'action', 'tenant_id',
                                'key', 'value'])
        return body


class UpdateL7policy(neutronV20.UpdateCommand):
    """Update a given l7policy."""

    resource = 'l7policy'


class DeleteL7policy(neutronV20.DeleteCommand):
    """Delete a given l7policy."""

    resource = 'l7policy'
