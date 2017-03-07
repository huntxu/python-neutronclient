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


class ListL7rule(neutronV20.ListCommand):
    """List L7rules that belong to a given tenant."""

    resource = 'l7rule'
    list_columns = ['id', 'type', 'key', 'value',
                    'compare_type', 'compare_value',
                    'admin_state_up']
    pagination_support = True
    sorting_support = True


class ShowL7rule(neutronV20.ShowCommand):
    """Show information of a given l7rule."""

    resource = 'l7rule'


class CreateL7rule(neutronV20.CreateCommand):
    """Create a l7rule."""

    resource = 'l7rule'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            help=_('Set admin state up to false.'))
        parser.add_argument(
            '--type',
            required=True,
            choices=['backendServerId'],
            help=_('The type of l7rule.'))
        parser.add_argument(
            '--key',
            help=_('The keyword for l7rule type.'))
        parser.add_argument(
            '--value',
            help=_('The value of the l7rule type.'))
        parser.add_argument(
            '--compare-type', dest='compare_type',
            required=True,
            choices=['integerEq'],
            help=_('The compare type of l7rule type.'))
        parser.add_argument(
            '--compare-value', dest="compare_value",
            required=True,
            help=_('The compare value of l7rule compare-type value.'))

    def args2body(self, parsed_args):
        body = {
            self.resource: {
                'admin_state_up': parsed_args.admin_state,
            },
        }
        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['type', 'key', 'value',
                                'compare_type', 'compare_value'])
        return body


class UpdateL7rule(neutronV20.UpdateCommand):
    """Update a given l7rule."""

    resource = 'l7rule'


class DeleteL7rule(neutronV20.DeleteCommand):
    """Delete a given l7rule."""

    resource = 'l7rule'


class AssociateL7rule(neutronV20.NeutronCommand):
    """Create a mapping between a l7rule and a l7policy."""

    resource = 'l7rule'

    def get_parser(self, prog_name):
        parser = super(AssociateL7rule, self).get_parser(prog_name)
        parser.add_argument(
            'l7rule_id', metavar='L7RULE_ID',
            help=_('l7rule to associate.'))
        parser.add_argument(
            'l7policy_id', metavar='L7POLICY',
            help=_('ID of the l7policy to be associated with the l7rule.'))
        return parser

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        body = {'l7rule': {'id': parsed_args.l7rule_id}}
        l7policy_id = neutronV20.find_resourceid_by_name_or_id(
            neutron_client, 'l7policy', parsed_args.l7policy_id)
        neutron_client.associate_l7rule(l7policy_id, body)
        print((_('Associated l7rule '
                 '%s') % parsed_args.l7rule_id),
              file=self.app.stdout)


class DisassociateL7rule(neutronV20.NeutronCommand):
    """Remove a mapping from a l7rule to l7policy."""

    resource = 'l7rule'

    def get_parser(self, prog_name):
        parser = super(DisassociateL7rule, self).get_parser(prog_name)
        parser.add_argument(
            'l7rule_id', metavar='L7RULE_ID',
            help=_('L7rule to disassociate.'))
        parser.add_argument(
            'l7policy_id', metavar='L7POLICY',
            help=_('ID of the l7policy to be disassociated with the l7rule.'))
        return parser

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        l7policy_id = neutronV20.find_resourceid_by_name_or_id(
            neutron_client, 'l7policy', parsed_args.l7policy_id)
        neutron_client.disassociate_l7rule(l7policy_id,
                                           parsed_args.l7rule_id)
        print((_('Disassociated l7rule '
                 '%s') % parsed_args.l7rule_id),
              file=self.app.stdout)
