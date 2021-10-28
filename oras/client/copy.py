__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MIT"

import oras.utils
from oras.logger import logger
import docker
import sys

from oras.content import File, FileStore

store = FileStore()

def main(args, parser, extra, subparser):

    print("COPY")
    import IPython
    IPython.embed()


    # get the fromStr; it might also have a ':' to add options
    from_parts = args.from_string.split(":")
    to_parts = args.to_string.split(":")
    
    # Copying from files
    if from_parts[0] == "files":

        # Extra files provided in extra (need to test)
        descs = load_files(extra)

        # parse the manifest config
        manifest_config_parts = args.manifest_config.split(":")
        manifest_config_media_type = ""

        # If length is 1, we only have this
        manifest_config_path = manifest_config_parts[0]

        # if length is two, we also have the config media type
        if len(manifest_config_parts) == 2:
            manifest_config_media_type = manifest_config_parts[1]

        # Read in the manifest config
	from_file = File()

"""
	from_file.add("", manifest_config_media_type, manifest_config_path)

				configDesc, err := fromFile.Add("", manifestConfigMediaType, manifestConfigPath)

				if err != nil {
					return fmt.Errorf("unable to load manifest config: %v", err)
				}
				if _, err := fromFile.GenerateManifest(ref, &configDesc, descs...); err != nil {
					return fmt.Errorf("unable to generate root manifest: %s", err)
				}
				rootDesc, rootManifest, err := fromFile.Ref(ref)
				if err != nil {
					return err
				}
				log.Debugf("root manifest: %s %v %s", ref, rootDesc, rootManifest)
				from = fromFile


    elif from_parts[0] == "registry":
 
				from, err = content.NewRegistry(opts)
				if err != nil {
					return fmt.Errorf("could not create registry target: %v", err)
				}


    elif from_parts[0] == "oci":
				from, err = content.NewOCI(fromParts[1])
				if err != nil {
					return fmt.Errorf("could not read OCI layout at %s: %v", fromParts[1], err)
				}

    else:    

				return fmt.Errorf("unknown from argyment: %s", from)

    if to_parts[0] == "flies":
				to = content.NewFile(toParts[1])
    
    
    elif to_parts[0] == "registry":
    
				to, err = content.NewRegistry(opts)
				if err != nil {
					return fmt.Errorf("could not create registry target: %v", err)
				}

    elif to_parts[0] == 'oci':    

				to, err = content.NewOCI(toParts[1])
				if err != nil {
					return fmt.Errorf("could not read OCI layout at %s: %v", toParts[1], err)
    else:				}

		return fmt.Errorf("unknown from argyment: %s", from)


			}

    if manifestConfig != "" && fromParts[0] != "files" {
				return fmt.Errorf("only specify --manifest-config when using --from files")
			}
			return runCopy(ref, from, to)
		},
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
"""    
   
   
func runCopy(ref string, from, to target.Target) error {
	desc, err := oras.Copy(context.Background(), from, ref, to, "")
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %v", err)
		os.Exit(1)
	}
	fmt.Printf("%#v\n", desc)
	return nil
}

def load_files(files):
    """
    Load files into the store and return a list of descriptors
    """
    # Keep a list of descriptors
    descs = []    
    for file_ref in files:
        filename, media_type = oras.utils.parse_file_ref(file_ref)  
        name = os.path.abspath(filename)
        descs.append(store.add(name, media_type, filename))

    return descs
