from kserve import KServeClient
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


def test_example(capsys):
    resource = Resource(attributes={
        SERVICE_NAME: "kserve-opentelemetry-test"
    })
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    _ = KServeClient(config_file='./kserve/test/kubeconfig')
