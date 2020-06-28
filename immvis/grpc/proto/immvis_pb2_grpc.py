# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import immvis_pb2 as immvis__pb2


class ImmVisStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListAvailableDatasets = channel.unary_unary(
        '/ImmVis/ListAvailableDatasets',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=immvis__pb2.AvailableDatasetsList.FromString,
        )
    self.LoadDataset = channel.unary_unary(
        '/ImmVis/LoadDataset',
        request_serializer=immvis__pb2.LoadDatasetRequestMessage.SerializeToString,
        response_deserializer=immvis__pb2.DatasetMetadata.FromString,
        )
    self.GetDatasetToPlot = channel.unary_unary(
        '/ImmVis/GetDatasetToPlot',
        request_serializer=immvis__pb2.GetDatasetToPlotRequestMessage.SerializeToString,
        response_deserializer=immvis__pb2.DatasetToPlot.FromString,
        )


class ImmVisServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListAvailableDatasets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LoadDataset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDatasetToPlot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImmVisServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListAvailableDatasets': grpc.unary_unary_rpc_method_handler(
          servicer.ListAvailableDatasets,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=immvis__pb2.AvailableDatasetsList.SerializeToString,
      ),
      'LoadDataset': grpc.unary_unary_rpc_method_handler(
          servicer.LoadDataset,
          request_deserializer=immvis__pb2.LoadDatasetRequestMessage.FromString,
          response_serializer=immvis__pb2.DatasetMetadata.SerializeToString,
      ),
      'GetDatasetToPlot': grpc.unary_unary_rpc_method_handler(
          servicer.GetDatasetToPlot,
          request_deserializer=immvis__pb2.GetDatasetToPlotRequestMessage.FromString,
          response_serializer=immvis__pb2.DatasetToPlot.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ImmVis', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
