import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import google.cloud.grpc.devtools.clouderrorreporting.v1beta1.report_errors_service_pb2 as google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_report__errors__service__pb2
import google.cloud.grpc.devtools.clouderrorreporting.v1beta1.report_errors_service_pb2 as google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_report__errors__service__pb2


class ReportErrorsServiceStub(object):
  """An API for reporting error events.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ReportErrorEvent = channel.unary_unary(
        '/google.devtools.clouderrorreporting.v1beta1.ReportErrorsService/ReportErrorEvent',
        request_serializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_report__errors__service__pb2.ReportErrorEventRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_report__errors__service__pb2.ReportErrorEventResponse.FromString,
        )


class ReportErrorsServiceServicer(object):
  """An API for reporting error events.
  """

  def ReportErrorEvent(self, request, context):
    """Report an individual error event.

    This endpoint accepts <strong>either</strong> an OAuth token,
    <strong>or</strong> an
    <a href="https://support.google.com/cloud/answer/6158862">API key</a>
    for authentication. To use an API key, append it to the URL as the value of
    a `key` parameter. For example:
    <pre>POST https://clouderrorreporting.googleapis.com/v1beta1/projects/example-project/events:report?key=123ABC456</pre>
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReportErrorsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ReportErrorEvent': grpc.unary_unary_rpc_method_handler(
          servicer.ReportErrorEvent,
          request_deserializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_report__errors__service__pb2.ReportErrorEventRequest.FromString,
          response_serializer=google_dot_cloud_dot_grpc_dot_devtools_dot_clouderrorreporting_dot_v1beta1_dot_report__errors__service__pb2.ReportErrorEventResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.devtools.clouderrorreporting.v1beta1.ReportErrorsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
