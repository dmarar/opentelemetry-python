"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import opentelemetry.proto.resource.v1.resource_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class MetricConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_FIELD_NUMBER: builtins.int
    LAST_KNOWN_FINGERPRINT_FIELD_NUMBER: builtins.int
    last_known_fingerprint: builtins.bytes = ...

    @property
    def resource(self) -> opentelemetry.proto.resource.v1.resource_pb2.Resource: ...

    def __init__(self,
        *,
        resource : typing.Optional[opentelemetry.proto.resource.v1.resource_pb2.Resource] = ...,
        last_known_fingerprint : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"resource",b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"last_known_fingerprint",b"last_known_fingerprint",u"resource",b"resource"]) -> None: ...
global___MetricConfigRequest = MetricConfigRequest

class MetricConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Schedule(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class Pattern(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            EQUALS_FIELD_NUMBER: builtins.int
            STARTS_WITH_FIELD_NUMBER: builtins.int
            equals: typing.Text = ...
            starts_with: typing.Text = ...

            def __init__(self,
                *,
                equals : typing.Text = ...,
                starts_with : typing.Text = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"equals",b"equals",u"match",b"match",u"starts_with",b"starts_with"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"equals",b"equals",u"match",b"match",u"starts_with",b"starts_with"]) -> None: ...
            def WhichOneof(self, oneof_group: typing_extensions.Literal[u"match",b"match"]) -> typing_extensions.Literal["equals","starts_with"]: ...

        EXCLUSION_PATTERNS_FIELD_NUMBER: builtins.int
        INCLUSION_PATTERNS_FIELD_NUMBER: builtins.int
        PERIOD_SEC_FIELD_NUMBER: builtins.int
        period_sec: builtins.int = ...

        @property
        def exclusion_patterns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MetricConfigResponse.Schedule.Pattern]: ...

        @property
        def inclusion_patterns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MetricConfigResponse.Schedule.Pattern]: ...

        def __init__(self,
            *,
            exclusion_patterns : typing.Optional[typing.Iterable[global___MetricConfigResponse.Schedule.Pattern]] = ...,
            inclusion_patterns : typing.Optional[typing.Iterable[global___MetricConfigResponse.Schedule.Pattern]] = ...,
            period_sec : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"exclusion_patterns",b"exclusion_patterns",u"inclusion_patterns",b"inclusion_patterns",u"period_sec",b"period_sec"]) -> None: ...

    FINGERPRINT_FIELD_NUMBER: builtins.int
    SCHEDULES_FIELD_NUMBER: builtins.int
    SUGGESTED_WAIT_TIME_SEC_FIELD_NUMBER: builtins.int
    fingerprint: builtins.bytes = ...
    suggested_wait_time_sec: builtins.int = ...

    @property
    def schedules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MetricConfigResponse.Schedule]: ...

    def __init__(self,
        *,
        fingerprint : builtins.bytes = ...,
        schedules : typing.Optional[typing.Iterable[global___MetricConfigResponse.Schedule]] = ...,
        suggested_wait_time_sec : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"fingerprint",b"fingerprint",u"schedules",b"schedules",u"suggested_wait_time_sec",b"suggested_wait_time_sec"]) -> None: ...
global___MetricConfigResponse = MetricConfigResponse
