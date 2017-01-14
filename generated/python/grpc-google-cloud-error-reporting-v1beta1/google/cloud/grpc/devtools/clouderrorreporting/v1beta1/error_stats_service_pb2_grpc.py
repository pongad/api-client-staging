import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import google.cloud.grpc.devtools.clouderrorreporting.v1beta1.error_stats_service_pb2 as google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2
import google.cloud.grpc.devtools.clouderrorreporting.v1beta1.error_stats_service_pb2 as google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2
import google.cloud.grpc.devtools.clouderrorreporting.v1beta1.error_stats_service_pb2 as google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2
import google.cloud.grpc.devtools.clouderrorreporting.v1beta1.error_stats_service_pb2 as google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2
import google.cloud.grpc.devtools.clouderrorreporting.v1beta1.error_stats_service_pb2 as google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2
import google.cloud.grpc.devtools.clouderrorreporting.v1beta1.error_stats_service_pb2 as google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2


class ErrorStatsServiceStub(object):
  """An API for retrieving and managing error statistics as well as data for
  individual events.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListGroupStats = channel.unary_unary(
        '/google.devtools.clouderrorreporting.v1beta1.ErrorStatsService/ListGroupStats',
        request_serializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.ListGroupStatsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.ListGroupStatsResponse.FromString,
        )
    self.ListEvents = channel.unary_unary(
        '/google.devtools.clouderrorreporting.v1beta1.ErrorStatsService/ListEvents',
        request_serializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.ListEventsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.ListEventsResponse.FromString,
        )
    self.DeleteEvents = channel.unary_unary(
        '/google.devtools.clouderrorreporting.v1beta1.ErrorStatsService/DeleteEvents',
        request_serializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.DeleteEventsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.DeleteEventsResponse.FromString,
        )


class ErrorStatsServiceServicer(object):
  """An API for retrieving and managing error statistics as well as data for
  individual events.
  """

  def ListGroupStats(self, request, context):
    """Lists the specified groups.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListEvents(self, request, context):
    """Lists the specified events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteEvents(self, request, context):
    """Deletes all error events of a given project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ErrorStatsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListGroupStats': grpc.unary_unary_rpc_method_handler(
          servicer.ListGroupStats,
          request_deserializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.ListGroupStatsRequest.FromString,
          response_serializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.ListGroupStatsResponse.SerializeToString,
      ),
      'ListEvents': grpc.unary_unary_rpc_method_handler(
          servicer.ListEvents,
          request_deserializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.ListEventsRequest.FromString,
          response_serializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.ListEventsResponse.SerializeToString,
      ),
      'DeleteEvents': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteEvents,
          request_deserializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.DeleteEventsRequest.FromString,
          response_serializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_error__stats__service__pb2.DeleteEventsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.devtools.clouderrorreporting.v1beta1.ErrorStatsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
