# File generated from our OpenAPI spec by Stainless.

from . import resources, _load_client
from ._utils import LazyProxy


class ChatProxy(LazyProxy[resources.Chat]):
    def __load__(self) -> resources.Chat:
        return _load_client().chat


class EditsProxy(LazyProxy[resources.Edits]):
    def __load__(self) -> resources.Edits:
        return _load_client().edits


class FilesProxy(LazyProxy[resources.Files]):
    def __load__(self) -> resources.Files:
        return _load_client().files


class AudioProxy(LazyProxy[resources.Audio]):
    def __load__(self) -> resources.Audio:
        return _load_client().audio


class ImagesProxy(LazyProxy[resources.Images]):
    def __load__(self) -> resources.Images:
        return _load_client().images


class ModelsProxy(LazyProxy[resources.Models]):
    def __load__(self) -> resources.Models:
        return _load_client().models


class EmbeddingsProxy(LazyProxy[resources.Embeddings]):
    def __load__(self) -> resources.Embeddings:
        return _load_client().embeddings


class FineTunesProxy(LazyProxy[resources.FineTunes]):
    def __load__(self) -> resources.FineTunes:
        return _load_client().fine_tunes


class CompletionsProxy(LazyProxy[resources.Completions]):
    def __load__(self) -> resources.Completions:
        return _load_client().completions


class ModerationsProxy(LazyProxy[resources.Moderations]):
    def __load__(self) -> resources.Moderations:
        return _load_client().moderations


class FineTuningProxy(LazyProxy[resources.FineTuning]):
    def __load__(self) -> resources.FineTuning:
        return _load_client().fine_tuning


chat: resources.Chat = ChatProxy().__as_proxied__()
edits: resources.Edits = EditsProxy().__as_proxied__()
files: resources.Files = FilesProxy().__as_proxied__()
audio: resources.Audio = AudioProxy().__as_proxied__()
images: resources.Images = ImagesProxy().__as_proxied__()
models: resources.Models = ModelsProxy().__as_proxied__()
embeddings: resources.Embeddings = EmbeddingsProxy().__as_proxied__()
fine_tunes: resources.FineTunes = FineTunesProxy().__as_proxied__()
completions: resources.Completions = CompletionsProxy().__as_proxied__()
moderations: resources.Moderations = ModerationsProxy().__as_proxied__()
fine_tuning: resources.FineTuning = FineTuningProxy().__as_proxied__()