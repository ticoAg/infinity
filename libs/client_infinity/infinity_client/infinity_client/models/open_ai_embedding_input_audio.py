from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embedding_encoding_format import EmbeddingEncodingFormat
from ..models.open_ai_embedding_input_audio_modality import OpenAIEmbeddingInputAudioModality
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenAIEmbeddingInputAudio")


@_attrs_define
class OpenAIEmbeddingInputAudio:
    """
    Attributes:
        input_ (Union[List[str], str]):
        model (Union[Unset, str]):  Default: 'default/not-specified'.
        encoding_format (Union[Unset, EmbeddingEncodingFormat]):
        user (Union[None, Unset, str]):
        dimensions (Union[Unset, int]):  Default: 0.
        modality (Union[Unset, OpenAIEmbeddingInputAudioModality]):  Default: OpenAIEmbeddingInputAudioModality.AUDIO.
    """

    input_: Union[List[str], str]
    model: Union[Unset, str] = "default/not-specified"
    encoding_format: Union[Unset, EmbeddingEncodingFormat] = UNSET
    user: Union[None, Unset, str] = UNSET
    dimensions: Union[Unset, int] = 0
    modality: Union[Unset, OpenAIEmbeddingInputAudioModality] = OpenAIEmbeddingInputAudioModality.AUDIO
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_: Union[List[str], str]
        if isinstance(self.input_, list):
            input_ = []
            for input_type_0_item_data in self.input_:
                input_type_0_item: str
                input_type_0_item = input_type_0_item_data
                input_.append(input_type_0_item)

        else:
            input_ = self.input_

        model = self.model

        encoding_format: Union[Unset, str] = UNSET
        if not isinstance(self.encoding_format, Unset):
            encoding_format = self.encoding_format.value

        user: Union[None, Unset, str]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        dimensions = self.dimensions

        modality: Union[Unset, str] = UNSET
        if not isinstance(self.modality, Unset):
            modality = self.modality.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if encoding_format is not UNSET:
            field_dict["encoding_format"] = encoding_format
        if user is not UNSET:
            field_dict["user"] = user
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if modality is not UNSET:
            field_dict["modality"] = modality

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_input_(data: object) -> Union[List[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_type_0 = []
                _input_type_0 = data
                for input_type_0_item_data in _input_type_0:

                    def _parse_input_type_0_item(data: object) -> str:
                        return cast(str, data)

                    input_type_0_item = _parse_input_type_0_item(input_type_0_item_data)

                    input_type_0.append(input_type_0_item)

                return input_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], str], data)

        input_ = _parse_input_(d.pop("input"))

        model = d.pop("model", UNSET)

        _encoding_format = d.pop("encoding_format", UNSET)
        encoding_format: Union[Unset, EmbeddingEncodingFormat]
        if isinstance(_encoding_format, Unset):
            encoding_format = UNSET
        else:
            encoding_format = EmbeddingEncodingFormat(_encoding_format)

        def _parse_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user = _parse_user(d.pop("user", UNSET))

        dimensions = d.pop("dimensions", UNSET)

        _modality = d.pop("modality", UNSET)
        modality: Union[Unset, OpenAIEmbeddingInputAudioModality]
        if isinstance(_modality, Unset):
            modality = UNSET
        else:
            modality = OpenAIEmbeddingInputAudioModality(_modality)

        open_ai_embedding_input_audio = cls(
            input_=input_,
            model=model,
            encoding_format=encoding_format,
            user=user,
            dimensions=dimensions,
            modality=modality,
        )

        open_ai_embedding_input_audio.additional_properties = d
        return open_ai_embedding_input_audio

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
