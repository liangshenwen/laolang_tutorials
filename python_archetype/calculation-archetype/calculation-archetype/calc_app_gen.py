import argparse
import os


class Archetype:
    def __init__(self):
        pass

    def create(self,
               project_name: str,
               project_folder: str, python_version: str, calc_sdk_version: str,
               starflow_version: str,
               metaflow_version: str,
               delete_if_exist: bool,
               template_folder: str = os.path.join(os.getcwd(), "template"),
               ) -> str:
        print(f'project_name:{project_name}')
        print(f'project_folder:{project_folder}')
        print(f'python_version:{python_version}')
        print(f'calc_sdk_version:{calc_sdk_version}')
        print(f'starflow_version:{starflow_version}')
        print(f'metaflow_version:{metaflow_version}')
        print(f'delete_if_exist:{delete_if_exist}')
        print(f'template_folder:{template_folder}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a poetry compatible calculation project using calculation-sdk")
    parser.add_argument(
        "-pn",
        "--project-name",
        dest="project_name",
        help="The name for project.",
        required=True
    )

    parser.add_argument(
        "-csv",
        "--calc-sdk-version",
        dest="calc_sdk_version",
        help="The version for calculation-sdk (e.g. 2.8.1).",
        required=True
    )

    parser.add_argument(
        "-pf",
        "--project-folder",
        dest="project_folder",
        default=os.path.expanduser('~'),
        help="The folder for the project."
    )

    parser.add_argument(
        "-pv",
        "--python-version",
        dest="python_version",
        default='3.7',
        help="The version for python (e.g. 3.7 or 3.9)."
    )

    parser.add_argument(
        "-sfv",
        "--starflow-version",
        dest="starflow_version",
        default='2.8.1',
        help="The version for starflow (e.g. 2.7.1)."
    )

    parser.add_argument(
        "-mfv",
        "--metaflow-version",
        dest="metaflow_version",
        default='2.7.1',
        help="The version for metaflow (e.g. 2.7.1)."
    )

    parser.add_argument(
        "-D",
        "--delete-if-exist",
        dest="delete_if_exist",
        action='store_true',
        help="If there is a project with the same name in the folder, delete it."
    )

    args = parser.parse_args()

    archetype = Archetype()
    result = archetype.create(args.project_name,
                              args.project_folder,
                              args.python_version,
                              args.calc_sdk_version,
                              args.starflow_version,
                              args.metaflow_version,
                              args.delete_if_exist)
    if result == '':
        print(f'Create project successfully in {args.project_folder}.')
    else:
        print(f'Create project successfully. Error message:{result}')
