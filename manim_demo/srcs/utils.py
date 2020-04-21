
import manimlib.extract_scene
import manimlib.constants
import manimlib.config
import argparse
from manimlib.extract_scene import *


def my_argparse( l=True, m=False, h=False, gif = False):
    try:
        parser = argparse.ArgumentParser()
        module_location = parser.add_mutually_exclusive_group()
        module_location.add_argument(
            "file",
            default= sys.argv[0],
            nargs="?",
            help="path to file holding the python code for the scene",
        )
        parser.add_argument(
            "scene_names",
            default= ['zz'],
            nargs="*",
            help="Name of the Scene class you want to see",
        )
        parser.add_argument(
            "-p", "--preview",
            default= True,
            action="store_true",
            help="Automatically open the saved file once its done",
        ),
        parser.add_argument(
            "-w", "--write_to_movie",
            action="store_true",
            help="Render the scene as a movie file",
        ),
        parser.add_argument(
            "-s", "--save_last_frame",
            action="store_true",
            help="Save the last frame",
        ),
        parser.add_argument(
            "-l", "--low_quality",
            default= l,
            action="store_true",
            help="Render at a low quality (for faster rendering)",
        ),
        parser.add_argument(
            "-m", "--medium_quality",
            default=m,
            action="store_true",
            help="Render at a medium quality",
        ),
        parser.add_argument(
            "--high_quality",
            default=h,
            action="store_true",
            help="Render at a high quality",
        ),
        parser.add_argument(
            "-g", "--save_pngs",
            action="store_true",
            help="Save each frame as a png",
        ),
        parser.add_argument(
            "-i", "--save_as_gif",
            default= gif,
            action="store_true",
            help="Save the video as gif",
        ),
        parser.add_argument(
            "-f", "--show_file_in_finder",
            action="store_true",
            help="Show the output file in finder",
        ),
        parser.add_argument(
            "-t", "--transparent",
            action="store_true",
            help="Render to a movie file with an alpha channel",
        ),
        parser.add_argument(
            "-q", "--quiet",
            action="store_true",
            help="",
        ),
        parser.add_argument(
            "-a", "--write_all",
            action="store_true",
            help="Write all the scenes from a file",
        ),
        parser.add_argument(
            "-o", "--file_name",
            help="Specify the name of the output file, if"
                 "it should be different from the scene class name",
        )
        parser.add_argument(
            "-n", "--start_at_animation_number",
            help="Start rendering not from the first animation, but"
                 "from another, specified by its index.  If you pass"
                 "in two comma separated values, e.g. \"3,6\", it will end"
                 "the rendering at the second value",
        )
        parser.add_argument(
            "-r", "--resolution",
            help="Resolution, passed as \"height,width\"",
        )
        parser.add_argument(
            "-c", "--color",
            help="Background color",
        )
        parser.add_argument(
            "--sound",
            action="store_true",
            help="Play a success/failure sound",
        )
        parser.add_argument(
            "--leave_progress_bars",
            action="store_true",
            help="Leave progress bars displayed in terminal",
        )
        parser.add_argument(
            "--media_dir",
            help="directory to write media",
        )
        video_group = parser.add_mutually_exclusive_group()
        video_group.add_argument(
            "--video_dir",
            default="./results/video/",
            help="directory to write file tree for video",
        )
        video_group.add_argument(
            "--video_output_dir",
            help="directory to write video",
        )
        parser.add_argument(
            "--tex_dir",
            default="./results",
            help="directory to write tex",
        )

        # For live streaming
        module_location.add_argument(
            "--livestream",
            action="store_true",
            help="Run in streaming mode",
        )
        parser.add_argument(
            "--to-twitch",
            action="store_true",
            help="Stream to twitch",
        )
        parser.add_argument(
            "--with-key",
            dest="twitch_key",
            help="Stream key for twitch",
        )
        args = parser.parse_args()

        if args.file is None and not args.livestream:
            parser.print_help()
            sys.exit(2)
        if args.to_twitch and not args.livestream:
            print("You must run in streaming mode in order to stream to twitch")
            sys.exit(2)
        if args.to_twitch and args.twitch_key is None:
            print("Specify the twitch stream key with --with-key")
            sys.exit(2)
        return args
    except argparse.ArgumentError as err:
        print(str(err))
        sys.exit(2)



def manim_main(config):

    scene_classes_to_render = config["module"]
    scene_kwargs = dict([
        (key, config[key])
        for key in [
            "camera_config",
            "file_writer_config",
            "skip_animations",
            "start_at_animation_number",
            "end_at_animation_number",
            "leave_progress_bars",
        ]
    ])

    for SceneClass in scene_classes_to_render:
        try:
            # By invoking, this renders the full scene
            scene = SceneClass(**scene_kwargs)
            open_file_if_needed(scene.file_writer, **config)
            if config["sound"]:
                play_finish_sound()
        except Exception:
            print("\n\n")
            traceback.print_exc()
            print("\n\n")
            if config["sound"]:
                play_error_sound()


def run( your_module, l=True, m=False, h=False, gif = False):
    """
    :param your_module: [your name class]
    :return:
    """
    args = my_argparse(l, m, h, gif)
    config = manimlib.config.get_configuration(args)
    config['module'] = your_module
    manimlib.constants.initialize_directories(config)
    manim_main(config)