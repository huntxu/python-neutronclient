# Copyright (c) 2017 Eayun, Inc.
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

from __future__ import print_function

from neutronclient.neutron import v2_0 as neutronv20
from neutronclient.openstack.common.gettextutils import _


class ListEsAcl(neutronv20.ListCommand):
    """Fetches a list of all EayunStack ACLs for a tenant."""

    resource = 'es_acl'
    list_columns = ['id', 'name', 'subnets', 'ingress_rules', 'egress_rules']
    pagination_support = True
    sorting_support = True


class ShowEsAcl(neutronv20.ShowCommand):
    """Fetch information of a certain EayunStack ACL."""

    resource = 'es_acl'
    allow_names = True


class CreateEsAcl(neutronv20.CreateCommand):
    """Create a new EayunStack ACL."""

    resource = 'es_acl'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name of this EayunStack ACL.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}}
        if parsed_args.name:
            body[self.resource].update({'name': parsed_args.name})
        if parsed_args.tenant_id:
            body[self.resource].update({'tenant_id': parsed_args.tenant_id})
        return body


class UpdateEsAcl(neutronv20.UpdateCommand):
    """Update a given EayunStack ACL."""

    resource = 'es_acl'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name of this EayunStack ACL.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}}
        if parsed_args.name:
            body[self.resource].update({'name': parsed_args.name})
        return body


class DeleteEsAcl(neutronv20.DeleteCommand):
    """Delete a given EayunStack ACL."""

    resource = 'es_acl'
    allow_names = True


class EsAclBindSubnets(neutronv20.UpdateCommand):
    """Bind a given EayunStack ACL to subnets."""

    resource = 'es_acl'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'subnets', metavar='SUBNETS',
            help=_('Subnets to bind this EayunStack ACL to.'))

    def args2body(self, parsed_args):
        body = {'subnet_ids': parsed_args.subnets.split(',')}
        return body

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        body = self.args2body(parsed_args)
        _id = neutronv20.find_resourceid_by_name_or_id(
            neutron_client, self.resource, parsed_args.id)
        neutron_client.es_acl_bind_subnets(_id, body)
        print((_("Bound EayunStack ACL %(id)s to subnets.") %
               {'id': parsed_args.id}), file=self.app.stdout)


class EsAclUnbindSubnets(neutronv20.UpdateCommand):
    """Unbind a given EayunStack ACL from subnets."""

    resource = 'es_acl'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'subnets', metavar='SUBNETS',
            help=_('Subnets to unbind this EayunStack ACL from.'))

    def args2body(self, parsed_args):
        body = {'subnet_ids': parsed_args.subnets.split(',')}
        return body

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        body = self.args2body(parsed_args)
        _id = neutronv20.find_resourceid_by_name_or_id(
            neutron_client, self.resource, parsed_args.id)
        neutron_client.es_acl_unbind_subnets(_id, body)
        print((_("Unbound EayunStack ACL %(id)s from subnets.") %
               {'id': parsed_args.id}), file=self.app.stdout)


class ListEsAclRule(neutronv20.ListCommand):
    """Fetches a list of all EayunStack ACL rules for a tenant."""

    resource = 'es_acl_rule'
    list_columns = ['id', 'name', 'acl_id', 'position', 'direction',
                    'protocol', 'source_ip_address', 'destination_ip_address',
                    'source_port', 'destination_port', 'action']
    pagination_support = True
    sorting_support = True


class ShowEsAclRule(neutronv20.ShowCommand):
    """Fetch information of a certain EayunStack ACL rule."""

    resource = 'es_acl_rule'
    allow_names = True


class CreateEsAclRule(neutronv20.CreateCommand):
    """Create a new EayunStack ACL rule."""

    resource = 'es_acl_rule'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'direction', metavar='DIRECTION',
            help=_('Direction of this EayunStack ACL rule.'))
        parser.add_argument(
            'action', metavar='ACTION',
            help=_('Action of this EayunStack ACL rule.'))
        parser.add_argument(
            '--name',
            help=_('Name of this EayunStack ACL rule.'))
        parser.add_argument(
            '--acl-id',
            help=_('Which EayunStack ACL should this EayunStack ACL rule '
                   'belong to.'))
        parser.add_argument(
            '--position',
            help=_('The position of this EayunStack ACL rule in its ACL.'))
        parser.add_argument(
            '--protocol',
            help=_('What protocol this this EayunStack ACL rule applies.'))
        parser.add_argument(
            '--src-ip',
            help=_('Source IP address of this EayunStack ACL rule.'))
        parser.add_argument(
            '--dst-ip',
            help=_('Destination IP address of this EayunStack ACL rule.'))
        parser.add_argument(
            '--src-port',
            help=_('Source port (range) of this EayunStack ACL rule.'))
        parser.add_argument(
            '--dst-port',
            help=_('Destination port (range) of this EayunStack ACL rule.'))

    def args2body(self, parsed_args):
        body = {self.resource: {'direction': parsed_args.direction,
                                'action': parsed_args.action}}
        if parsed_args.tenant_id:
            body[self.resource].update({'tenant_id': parsed_args.tenant_id})
        if parsed_args.name:
            body[self.resource].update({'name': parsed_args.name})
        if parsed_args.acl_id:
            body[self.resource].update({'acl_id': parsed_args.acl_id})
        if parsed_args.position:
            body[self.resource].update({'position': parsed_args.position})
        if parsed_args.protocol:
            body[self.resource].update({'protocol': parsed_args.protocol})
        if parsed_args.src_ip:
            body[self.resource].update(
                {'source_ip_address': parsed_args.src_ip})
        if parsed_args.dst_ip:
            body[self.resource].update(
                {'destination_ip_address': parsed_args.dst_ip})
        if parsed_args.src_port:
            body[self.resource].update(
                {'source_port': parsed_args.src_port})
        if parsed_args.dst_port:
            body[self.resource].update(
                {'destination_port': parsed_args.dst_port})
        return body


class UpdateEsAclRule(neutronv20.UpdateCommand):
    """Update a given EayunStack ACL rule."""

    resource = 'es_acl_rule'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name of this EayunStack ACL rule.'))
        parser.add_argument(
            '--acl-id',
            help=_('Which EayunStack ACL should this EayunStack ACL rule '
                   'belong to.'))
        parser.add_argument(
            '--position',
            help=_('The position of this EayunStack ACL rule in its ACL.'))
        parser.add_argument(
            '--direction', metavar='DIRECTION',
            help=_('Direction of this EayunStack ACL rule.'))
        parser.add_argument(
            '--protocol',
            help=_('What protocol this this EayunStack ACL rule applies.'))
        parser.add_argument(
            '--src-ip',
            help=_('Source IP address of this EayunStack ACL rule.'))
        parser.add_argument(
            '--dst-ip',
            help=_('Destination IP address of this EayunStack ACL rule.'))
        parser.add_argument(
            '--src-port',
            help=_('Source port (range) of this EayunStack ACL rule.'))
        parser.add_argument(
            '--dst-port',
            help=_('Destination port (range) of this EayunStack ACL rule.'))
        parser.add_argument(
            '--action', metavar='ACTION',
            help=_('Action of this EayunStack ACL rule.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}}

        if parsed_args.name:
            body[self.resource].update({'name': parsed_args.name})
        if parsed_args.acl_id:
            body[self.resource].update({'acl_id': parsed_args.acl_id})
        if parsed_args.position:
            body[self.resource].update({'position': parsed_args.position})
        if parsed_args.direction:
            body[self.resource].update({'direction': parsed_args.direction})
        if parsed_args.protocol:
            body[self.resource].update({'protocol': parsed_args.protocol})
        if parsed_args.src_ip:
            body[self.resource].update(
                {'source_ip_address': parsed_args.src_ip})
        if parsed_args.dst_ip:
            body[self.resource].update(
                {'destination_ip_address': parsed_args.dst_ip})
        if parsed_args.src_port:
            body[self.resource].update(
                {'source_port': parsed_args.src_port})
        if parsed_args.dst_port:
            body[self.resource].update(
                {'destination_port': parsed_args.dst_port})
        if parsed_args.action:
            body[self.resource].update({'action': parsed_args.action})
        return body


class DeleteEsAclRule(neutronv20.DeleteCommand):
    """Delete a given EayunStack ACL rule."""

    resource = 'es_acl_rule'
    allow_names = True
