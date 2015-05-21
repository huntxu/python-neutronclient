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

import argparse
import six

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListQos(neutronV20.ListCommand):
    """List Qos."""

    resource = "qos"
    shadow_resource = "eayun_qos"
    list_columns = ['id', 'name', 'description',
                    'direction', 'target_type', 'target_id',
                    'rate', 'burst', 'cburst', 'default_queue_id']
    pagination_support = True
    sorting_support = True


class ShowQos(neutronV20.ShowCommand):
    """Show information of a given qos."""

    resource = "qos"
    shadow_resource = "eayun_qos"
    allow_names = True
    ids_only = ['qos_queues', 'unattached_filters']

    def format_output_data(self, data):
        if self.resource in data:
            for k, v in six.iteritems(data[self.resource]):
                if k in self.ids_only and isinstance(v, list):
                    data[self.resource][k] = [item['id'] for item in v]

        super(ShowQos, self).format_output_data(data)


class CreateQos(neutronV20.CreateCommand):
    """Create a qos."""

    resource = "qos"
    shadow_resource = "eayun_qos"

    ids_only = ['qos_queues', 'unattached_filters']

    def format_output_data(self, data):
        if self.resource in data:
            for k, v in six.iteritems(data[self.resource]):
                if k in self.ids_only and isinstance(v, list):
                    data[self.resource][k] = [item['id'] for item in v]

        super(CreateQos, self).format_output_data(data)

    def add_known_arguments(self, parser):
        parser.add_argument(
            'direction', metavar='DIRECTION',
            help=_('Direction of this qos: "ingress" or "egress".'))
        parser.add_argument(
            'rate', metavar='RATE',
            help=_('Rate of this qos.'))
        parser.add_argument(
            'default_rate', metavar='DEFAULT_RATE',
            help=_('Rate of default queue of this qos.'))
        parser.add_argument(
            '--name',
            help=_('Name of this qos.'))
        parser.add_argument(
            '--description',
            help=_('Description of this qos.'))
        parser.add_argument(
            '--target-type',
            help=_('Target type of this qos: "router" or "port".'))
        parser.add_argument(
            '--target_type',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--target-id',
            help=_('Target id of this qos: "router" or "port".'))
        parser.add_argument(
            '--target_id',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--burst',
            help=_('Burst of this qos.'))
        parser.add_argument(
            '--cburst',
            help=_('Cburst of this qos.'))
        parser.add_argument(
            '--default-burst',
            help=_('Burst of default queue of this qos.'))
        parser.add_argument(
            '--default_burst',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--default-cburst',
            help=_('Cburst of default queue of this qos.'))
        parser.add_argument(
            '--default_cburst',
            help=argparse.SUPPRESS)

    def args2body(self, parsed_args):
        body = {
            'qos': {
                'direction': parsed_args.direction,
                'rate': parsed_args.rate,
                'default_rate': parsed_args.default_rate,
            }
        }
        if parsed_args.name:
            body['qos'].update({'name': parsed_args.name})
        if parsed_args.description:
            body['qos'].update({'description': parsed_args.description})
        if parsed_args.target_type:
            body['qos'].update({'target_type': parsed_args.target_type})
        if parsed_args.target_id:
            body['qos'].update({'target_id': parsed_args.target_id})
        if parsed_args.burst:
            body['qos'].update({'burst': parsed_args.burst})
        if parsed_args.cburst:
            body['qos'].update({'cburst': parsed_args.cburst})
        if parsed_args.default_burst:
            body['qos'].update({'default_burst': parsed_args.default_burst})
        if parsed_args.default_cburst:
            body['qos'].update({'default_cburst': parsed_args.default_cburst})
        return body


class UpdateQos(neutronV20.UpdateCommand):
    """Update a given qos."""

    resource = "qos"
    shadow_resource = "eayun_qos"

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name',
            help=_('Name of this qos.'))
        parser.add_argument(
            '--description',
            help=_('Description of this qos.'))
        parser.add_argument(
            '--target-type',
            help=_('Target type of this qos: "router" or "port".'))
        parser.add_argument(
            '--target_type',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--target-id',
            help=_('Target id of this qos: "router" or "port".'))
        parser.add_argument(
            '--target_id',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--rate',
            help=_('Rate of this qos.'))
        parser.add_argument(
            '--burst',
            help=_('Burst of this qos.'))
        parser.add_argument(
            '--cburst',
            help=_('Cburst of this qos.'))
        parser.add_argument(
            '--default-rate',
            help=_('Rate of default queue of this qos.'))
        parser.add_argument(
            '--default_rate',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--default-burst',
            help=_('Burst of default queue of this qos.'))
        parser.add_argument(
            '--default_burst',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--default-cburst',
            help=_('Cburst of default queue of this qos.'))
        parser.add_argument(
            '--default_cburst',
            help=argparse.SUPPRESS)

    def args2body(self, parsed_args):
        body = {'qos': {}}
        if parsed_args.name:
            body['qos'].update({'name': parsed_args.name})
        if parsed_args.description:
            body['qos'].update({'description': parsed_args.description})
        if parsed_args.target_type:
            body['qos'].update({'target_type': parsed_args.target_type})
        if parsed_args.target_id:
            body['qos'].update({'target_id': parsed_args.target_id})
        if parsed_args.rate:
            body['qos'].update({'rate': parsed_args.rate})
        if parsed_args.burst:
            body['qos'].update({'burst': parsed_args.burst})
        if parsed_args.cburst:
            body['qos'].update({'cburst': parsed_args.cburst})
        if parsed_args.default_rate:
            body['qos'].update({'default_rate': parsed_args.default_rate})
        if parsed_args.default_burst:
            body['qos'].update({'default_burst': parsed_args.default_burst})
        if parsed_args.default_cburst:
            body['qos'].update({'default_cburst': parsed_args.default_cburst})
        return body


class DeleteQos(neutronV20.DeleteCommand):
    """Delete a given qos."""

    resource = "qos"
    shadow_resource = "eayun_qos"


class UnbindQos(UpdateQos):
    """Unbind a given qos from its target."""

    def args2body(self, parsed_args):
        return {'qos': {'target_type': None, 'target_id': None}}


class ListQosQueue(neutronV20.ListCommand):
    """List Qos queue."""

    resource = "qos_queue"
    shadow_resource = "eayun_qos_queue"
    list_columns = ['id', 'qos_id', 'parent_id',
                    'prio', 'rate', 'ceil', 'burst', 'cburst']
    pagination_support = True
    sorting_support = True


class ShowQosQueue(neutronV20.ShowCommand):
    """Show information of a given qos queue."""

    resource = "qos_queue"
    shadow_resource = "eayun_qos_queue"
    allow_names = False
    ids_only = ['subqueues', 'attached_filters']

    def format_output_data(self, data):
        if self.resource in data:
            for k, v in six.iteritems(data[self.resource]):
                if k in self.ids_only and isinstance(v, list):
                    data[self.resource][k] = [item['id'] for item in v]

        super(ShowQosQueue, self).format_output_data(data)


class CreateQosQueue(neutronV20.CreateCommand):
    """Create a qos queue."""

    resource = "qos_queue"
    shadow_resource = "eayun_qos_queue"
    ids_only = ['subqueues', 'attached_filters']

    def format_output_data(self, data):
        if self.resource in data:
            for k, v in six.iteritems(data[self.resource]):
                if k in self.ids_only and isinstance(v, list):
                    data[self.resource][k] = [item['id'] for item in v]

        super(CreateQosQueue, self).format_output_data(data)

    def add_known_arguments(self, parser):
        parser.add_argument(
            'qos', metavar='QOS',
            help=_('Qos to which this qos queue belongs.'))
        parser.add_argument(
            'rate', metavar='RATE',
            help=_('Rate of this qos queue.'))
        parser.add_argument(
            '--parent',
            help=_('Parent qos queue of this qos queue.'))
        parser.add_argument(
            '--prio',
            help=_('Prio of this qos queue.'))
        parser.add_argument(
            '--ceil',
            help=_('Ceil of this qos.'))
        parser.add_argument(
            '--burst',
            help=_('Burst of this qos.'))
        parser.add_argument(
            '--cburst',
            help=_('Cburst of this qos.'))

    def args2body(self, parsed_args):
        body = {
            'qos_queue': {
                'qos_id': parsed_args.qos,
                'rate': parsed_args.rate,
            }
        }
        if parsed_args.parent:
            body['qos_queue'].update({'parent_id': parsed_args.parent})
        if parsed_args.prio:
            body['qos_queue'].update({'prio': parsed_args.prio})
        if parsed_args.ceil:
            body['qos_queue'].update({'ceil': parsed_args.ceil})
        if parsed_args.burst:
            body['qos_queue'].update({'burst': parsed_args.burst})
        if parsed_args.cburst:
            body['qos_queue'].update({'cburst': parsed_args.cburst})
        return body


class UpdateQosQueue(neutronV20.UpdateCommand):
    """Update a given qos queue."""

    resource = "qos_queue"
    shadow_resource = "eayun_qos_queue"
    allow_names = False

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--prio',
            help=_('Prio of this qos queue.'))
        parser.add_argument(
            '--rate',
            help=_('Rate of this qos queue.'))
        parser.add_argument(
            '--ceil',
            help=_('Ceil of this qos.'))
        parser.add_argument(
            '--burst',
            help=_('Burst of this qos.'))
        parser.add_argument(
            '--cburst',
            help=_('Cburst of this qos.'))

    def args2body(self, parsed_args):
        body = {'qos_queue': {}}
        if parsed_args.prio:
            body['qos_queue'].update({'prio': parsed_args.prio})
        if parsed_args.rate:
            body['qos_queue'].update({'rate': parsed_args.ceil})
        if parsed_args.ceil:
            body['qos_queue'].update({'ceil': parsed_args.ceil})
        if parsed_args.burst:
            body['qos_queue'].update({'burst': parsed_args.burst})
        if parsed_args.cburst:
            body['qos_queue'].update({'cburst': parsed_args.cburst})
        return body


class DeleteQosQueue(neutronV20.DeleteCommand):
    """Delete a given qos queue."""

    resource = "qos_queue"
    shadow_resource = "eayun_qos_queue"
    allow_names = False


class ListQosFilter(neutronV20.ListCommand):
    """List Qos filter."""

    resource = "qos_filter"
    shadow_resource = "eayun_qos_filter"
    list_columns = ['id', 'qos_id', 'queue_id', 'prio',
                    'protocol', 'src_port', 'dst_port',
                    'src_addr', 'dst_addr', 'custom_match']
    pagination_support = True
    sorting_support = True


class ShowQosFilter(neutronV20.ShowCommand):
    """Show information of a given qos filter."""

    resource = "qos_filter"
    shadow_resource = "eayun_qos_filter"
    allow_names = False


class CreateQosFilter(neutronV20.CreateCommand):
    """Create a qos filter."""

    resource = "qos_filter"
    shadow_resource = "eayun_qos_filter"

    def add_known_arguments(self, parser):
        parser.add_argument(
            'qos', metavar='QOS',
            help=_('Qos to which this qos filter belongs.'))
        parser.add_argument(
            'prio', metavar="PRIO",
            help=_('Prio of this qos filter.'))
        parser.add_argument(
            '--queue',
            help=_('Qos queue to which this qos filter is attached.'))
        parser.add_argument(
            '--protocol',
            help=_('Protocol this qos filter is to match.'))
        parser.add_argument(
            '--src-port',
            help=_('Source port this qos filter is to match.'))
        parser.add_argument(
            '--src_port',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--dst-port',
            help=_('Destination port this qos filter is to match.'))
        parser.add_argument(
            '--dst_port',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--src-addr',
            help=_('Source address(es) this qos filter is to match.'))
        parser.add_argument(
            '--src_addr',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--dst-addr',
            help=_('Destination address(es) this qos filter is to match.'))
        parser.add_argument(
            '--dst_addr',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--custom-match',
            help=_('Custom match rule of this qos filter.'))
        parser.add_argument(
            '--custom_match',
            help=argparse.SUPPRESS)

    def args2body(self, parsed_args):
        body = {
            'qos_filter': {
                'qos_id': parsed_args.qos,
                'prio': parsed_args.prio,
            }
        }
        if parsed_args.queue:
            body['qos_filter'].update({'queue_id': parsed_args.queue})
        if parsed_args.protocol:
            body['qos_filter'].update({'protocol': parsed_args.protocol})
        if parsed_args.src_port:
            body['qos_filter'].update({'src_port': parsed_args.src_port})
        if parsed_args.dst_port:
            body['qos_filter'].update({'dst_port': parsed_args.dst_port})
        if parsed_args.src_addr:
            body['qos_filter'].update({'src_addr': parsed_args.src_addr})
        if parsed_args.dst_addr:
            body['qos_filter'].update({'dst_addr': parsed_args.dst_addr})
        if parsed_args.custom_match:
            body['qos_filter'].update(
                {'custom_match': parsed_args.custom_match})
        return body


class UpdateQosFilter(neutronV20.UpdateCommand):
    """Update a given qos filter."""

    resource = "qos_filter"
    shadow_resource = "eayun_qos_filter"
    allow_names = False

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--queue',
            help=_('Qos queue to which this qos filter is attached.'))
        parser.add_argument(
            '--prio',
            help=_('Prio of this qos filter.'))
        parser.add_argument(
            '--protocol',
            help=_('Protocol this qos filter is to match.'))
        parser.add_argument(
            '--src-port',
            help=_('Source port this qos filter is to match.'))
        parser.add_argument(
            '--src_port',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--dst-port',
            help=_('Destination port this qos filter is to match.'))
        parser.add_argument(
            '--dst_port',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--src-addr',
            help=_('Source address(es) this qos filter is to match.'))
        parser.add_argument(
            '--src_addr',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--dst-addr',
            help=_('Destination address(es) this qos filter is to match.'))
        parser.add_argument(
            '--dst_addr',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--custom-match',
            help=_('Custom match rule of this qos filter.'))
        parser.add_argument(
            '--custom_match',
            help=argparse.SUPPRESS)

    def args2body(self, parsed_args):
        body = {'qos_filter': {}}
        if parsed_args.queue:
            body['qos_filter'].update({'queue_id': parsed_args.queue})
        if parsed_args.prio:
            body['qos_filter'].update({'prio': parsed_args.prio})
        if parsed_args.protocol:
            body['qos_filter'].update({'protocol': parsed_args.protocol})
        if parsed_args.src_port:
            body['qos_filter'].update({'src_port': parsed_args.src_port})
        if parsed_args.dst_port:
            body['qos_filter'].update({'dst_port': parsed_args.dst_port})
        if parsed_args.src_addr:
            body['qos_filter'].update({'src_addr': parsed_args.src_addr})
        if parsed_args.dst_addr:
            body['qos_filter'].update({'dst_addr': parsed_args.dst_addr})
        if parsed_args.custom_match:
            body['qos_filter'].update(
                {'custom_match': parsed_args.custom_match})
        return body


class DeleteQosFilter(neutronV20.DeleteCommand):
    """Delete a given qos filter."""

    resource = "qos_filter"
    shadow_resource = "eayun_qos_filter"
    allow_names = False


class UnattachQosFilter(UpdateQosFilter):
    """Unattach a given qos filter from queue."""

    def args2body(self, parsed_args):
        return {'qos_filter': {'queue_id': None}}
