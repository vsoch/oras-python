__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MIT"

import opencontainers.digest as digest
import opencontainers.image.v1 as ocispec

## TODO: these should be updated on release
# we could also generate them interactively. Thoughts?

# The state of the git tree
git_tree_state = ""

# Extra build time data
build_metadata = "unreleased"

# Git sha
git_commit = ""

# https://github.com/moby/moby/blob/master/registry/config.go#L29
class registry:
    index_hostname = "index.docker.io"
    index_server = "https://index.docker.io/v1/"
    index_name = "docker.io"
    default_v2_registry = {"scheme": "https", "host": "registry-1.docker.io"}
    

# DefaultBlobMediaType specifies the default blob media type
DefaultBlobMediaType = ocispec.MediaTypeImageLayer

# DefaultBlobDirMediaType specifies the default blob directory media type
DefaultBlobDirMediaType = ocispec.MediaTypeImageLayerGzip

# TempFilePattern specifies the pattern to create temporary files
TempFilePattern = "oras"

# AnnotationDigest is the annotation key for the digest of the uncompressed content
AnnotationDigest = "io.deis.oras.content.digest"

# AnnotationUnpack is the annotation key for indication of unpacking
AnnotationUnpack = "io.deis.oras.content.unpack"

# OCIImageIndexFile is the file name of the index from the OCI Image Layout Specification
# Reference: https://github.com/opencontainers/image-spec/blob/master/image-layout.md#indexjson-file
OCIImageIndexFile = "index.json"

# DefaultBlocksize default size of each slice of bytes read in each write through in gunzipand untar.
# Simply uses the same size as io.Copy()
DefaultBlocksize = 32768

# what you get for a blank digest
BlankHash = digest.Digest("sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
