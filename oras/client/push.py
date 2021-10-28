__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MIT"

from oras.logger import logger
import docker
import sys


def readline():
    """Read lines from stdin"""
    content = sys.stdin.readlines()
    return content[0].strip()


def main(args, parser, extra, subparser):

    # Annotations
    annotations = {}

func runPush(opts pushOptions) error {

	// load files
	var (
		store       = content.NewFileStore("")
		pushOpts    []oras.PushOpt
	)
	defer store.Close()
	if opts.manifestAnnotations != "" {
		if err := decodeJSON(opts.manifestAnnotations, &annotations); err != nil {
			return err
		}
		if value, ok := annotations[annotationConfig]; ok {
			pushOpts = append(pushOpts, oras.WithConfigAnnotations(value))
		}
		if value, ok := annotations[annotationManifest]; ok {
			pushOpts = append(pushOpts, oras.WithManifestAnnotations(value))
		}
	}
	if opts.manifestConfigRef != "" {
		filename, mediaType := parseFileRef(opts.manifestConfigRef, artifact.UnknownConfigMediaType)
		file, err := store.Add(annotationConfig, mediaType, filename)
		if err != nil {
			return err
		}
		file.Annotations = nil
		pushOpts = append(pushOpts, oras.WithConfig(file))
	}
	if opts.pathValidationDisabled {
		pushOpts = append(pushOpts, oras.WithNameValidation(nil))
	}
	files, err := loadFiles(store, annotations, &opts)
	if err != nil {
		return err
	}
	if len(files) == 0 {
		fmt.Println("Uploading empty artifact")
	}

	// ready to push
	resolver := newResolver(opts.username, opts.password, opts.insecure, opts.plainHTTP, opts.configs...)
	pushOpts = append(pushOpts, oras.WithPushStatusTrack(os.Stdout))
	desc, err := oras.Push(ctx, resolver, opts.targetRef, store, files, pushOpts...)
	if err != nil {
		return err
	}

	fmt.Println("Pushed", opts.targetRef)
	fmt.Println("Digest:", desc.Digest)

	return nil
}

func decodeJSON(filename string, v interface{}) error {
	file, err := os.Open(filename)
	if err != nil {
		return err
	}
	defer file.Close()
	return json.NewDecoder(file).Decode(v)
}

func loadFiles(store *content.FileStore, annotations map[string]map[string]string, opts *pushOptions) ([]ocispec.Descriptor, error) {
	var files []ocispec.Descriptor
	for _, fileRef := range opts.fileRefs {
		filename, mediaType := parseFileRef(fileRef, "")
		name := filepath.Clean(filename)
		if !filepath.IsAbs(name) {
			// convert to slash-separated path unless it is absolute path
			name = filepath.ToSlash(name)
		}
		if opts.verbose {
			fmt.Println("Preparing", name)
		}
		file, err := store.Add(name, mediaType, filename)
		if err != nil {
			return nil, err
		}
		if annotations != nil {
			if value, ok := annotations[filename]; ok {
				if file.Annotations == nil {
					file.Annotations = value
				} else {
					for k, v := range value {
						file.Annotations[k] = v
					}
				}
			}
		}
		files = append(files, file)
	}
	return files, nil
}







    client = docker.DockerClient(tls=not args.insecure)

    password = args.password
    username = args.username

    # Read password from stdin
    if args.password_stdin:
        password = readline()

    # No password provided
    elif not password:

        # No username, try to get from stdin
        if not username:
            username = input("Username: ")

        # if we still don't have a username, we require a token
        if not username:
            prompt = "Token: "
            password = input("Token: ")
            if not password:
                logger.exit("token required")

        # If we do have a username, we just need a passowrd
        else:
            password = input("Password: ")
            if not password:
                logger.exit("password required")

    else:
        logger.warning(
            "WARNING! Using --password via the CLI is insecure. Use --password-stdin."
        )

    # Login
    # https://docker-py.readthedocs.io/en/stable/client.html?highlight=login#docker.client.DockerClient.login
    result = client.login(
        username=username, password=password, registry=args.hostname, dockercfg_path=args.config
    )
    logger.info(result["Status"])
    
   
