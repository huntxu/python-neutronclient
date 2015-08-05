# Copyright 2015 Eayun, Inc.
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

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListPortmapping(neutronV20.ListCommand):
    """List portmappings."""

    resource = "portmapping"
    list_columns = ['id', 'name', 'status', 'router_id', 'destination_ip',
                    'protocol', 'admin_state_up', 'tenant_id',
                    'destination_port', 'router_port']
    pagination_support = True
    sorting_support = True


class ShowPortmapping(neutronV20.ShowCommand):
    """show information of a given portmapping."""

    resource = "portmapping"
    allow_names = True


class CreatePortmapping(neutronV20.CreateCommand):
    """Create a portmapping."""

    resource = "portmapping"

    def add_known_arguments(self, parser):
        parser.add_argument(
            'router_id', metavar='ROUTER_ID',
            help=_('The id of the router to be port-mapped.')
        )
        parser.add_argument(
            'router_port', metavar='ROUTER_PORT',
            help=_("The router's port number to be mapped.")
        )
        parser.add_argument(
            'destination_ip', metavar='DESTINATION_IP',
            help=_('The destination ip to be redirected to.')
        )
        parser.add_argument(
            'destination_port', metavar='DESTINATION_PORT',
            help=_('The destination port to be redirected to.')
        )
        parser.add_argument(
            '--name',
            help=_("The portmapping's name")
        )
        parser.add_argument(
            '--protocol',
            help=_('The protocol to be matched by this '
                   'portmapping, "TCP" or "UDP", default: TCP.')
        )

    def args2body(self, parsed_args):
        body = {
            'portmapping': {
                'router_id': parsed_args.router_id,
                'router_port': parsed_args.router_port,
                'destination_ip': parsed_args.destination_ip,
                'destination_port': parsed_args.destination_port,
            }
        }
        if parsed_args.name:
            body['portmapping'].update(
                {'name': parsed_args.name})
        if parsed_args.protocol:
            body['portmapping'].update(
                {'protocol': parsed_args.protocol})
        return body


class UpdatePortmapping(neutronV20.UpdateCommand):
    """Update a given portmapping."""

    resource = "portmapping"

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_("The portmapping's name."))

    def args2body(self, parsed_args):
        body = {'portmapping': {}}
        if parsed_args.name:
            body['portmapping'].update(
                {'name': parsed_args.name})
        return body


class DeletePortmapping(neutronV20.DeleteCommand):
    """Delete a given portmapping."""

    resource = "portmapping"
