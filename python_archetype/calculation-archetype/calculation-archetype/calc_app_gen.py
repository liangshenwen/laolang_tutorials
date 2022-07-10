import argparse
import os
import shutil

from jinja2.nativetypes import NativeEnvironment

ENCODING = 'UTF-8'

class Archetype:
    def __init__(self):
        pass

    def create(self,
               project_name: str,
               target_folder: str, python_version: str, calc_sdk_version: str,
               starflow_version: str,
               metaflow_version: str,
               delete_if_exist: bool,
               template_folder: str = os.path.join(os.getcwd(), 'template'),
               ) -> str:
        """
        Create a project based on the given project name.

        :param project_name: The name of project.
        :param target_folder: The target folder of project.
        :param python_version: The python version of project.
        :param calc_sdk_version: The version of calculation-sdk.
        :param starflow_version: The version of starflow.
        :param metaflow_version: The version of metaflow.
        :param delete_if_exist:  A flag to indicate that project should be deleted or not if it is existed.
        :param template_folder:  The folder of template.
        :return: The path where the project is created.
        """
        print(f'project_name:{project_name}')
        print(f'target_folder:{target_folder}')
        print(f'python_version:{python_version}')
        print(f'calc_sdk_version:{calc_sdk_version}')
        print(f'starflow_version:{starflow_version}')
        print(f'metaflow_version:{metaflow_version}')
        print(f'delete_if_exist:{delete_if_exist}')
        print(f'template_folder:{template_folder}')

        # if project_name is a valid python identifier.
        if project_name.isidentifier():
            project_path = os.path.join(target_folder, project_name)
            if os.path.exists(project_path):
                if delete_if_exist:
                    print(f'delete existing project folder `{project_path}`')
                    shutil.rmtree(project_path)
                    # create empty project folder
                    os.makedirs(project_path)
            else:
                # create empty project folder
                os.makedirs(project_path)

            # check whether project folder is empty or not.
            sub_files = os.listdir(project_path)
            if sub_files and len(sub_files) > 0:
                print(f'error: project folder ‘{project_path}’ must be empty.')
                return ''

            # create project from template
            shutil.copytree(template_folder, project_path, dirs_exist_ok=True)

            # render project
            data_dict = {
                'project_name': project_name,
                'python_version': python_version,
                'calc_sdk_version': calc_sdk_version,
                'starflow_version': starflow_version,
                'metaflow_version': metaflow_version
            }
            self.render_project(project_path, data_dict)

            return project_path

        else:
            print(f'error: project name ‘{project_name} ’ is invalid.')
            return ''

        return ''

    def render_project(self, project_path: str, data_dict: dict):
        env = NativeEnvironment()

        # render pyproject.toml
        toml_file = os.path.join(project_path, 'pyproject.toml')
        toml_file_content = ''
        with open(toml_file, 'r', encoding=ENCODING) as f:
            toml_file_content = env.from_string(f.read()).render(**data_dict)
        if toml_file_content != '':
            with open(toml_file, 'w', encoding=ENCODING) as f:
                f.write(toml_file_content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a poetry compatible calculation project using calculation-sdk')
    parser.add_argument(
        '-pn',
        '--project-name',
        dest='project_name',
        help='The name for project.',
        required=True
    )

    parser.add_argument(
        '-csv',
        '--calc-sdk-version',
        dest='calc_sdk_version',
        help='The version for calculation-sdk (e.g. 2.8.1).',
        required=True
    )

    parser.add_argument(
        '-pf',
        '--target-folder',
        dest='target_folder',
        default=os.path.expanduser('~'),
        help='The target folder for the project.'
    )

    parser.add_argument(
        '-pv',
        '--python-version',
        dest='python_version',
        default='3.7.0',
        help='The version for python (e.g. 3.7.0 or 3.9.0).'
    )

    parser.add_argument(
        '-sfv',
        '--starflow-version',
        dest='starflow_version',
        default='2.8.1',
        help='The version for starflow (e.g. 2.7.1).'
    )

    parser.add_argument(
        '-mfv',
        '--metaflow-version',
        dest='metaflow_version',
        default='2.2.5',
        help='The version for metaflow (e.g. 2.2.5 or 2.7.1).'
    )

    parser.add_argument(
        '-d',
        '--delete-if-exist',
        dest='delete_if_exist',
        action='store_true',
        help='If there is a project with the same name in the folder, delete it.'
    )

    args = parser.parse_args()

    archetype = Archetype()
    project_folder = archetype.create(args.project_name,
                                      args.target_folder,
                                      args.python_version,
                                      args.calc_sdk_version,
                                      args.starflow_version,
                                      args.metaflow_version,
                                      args.delete_if_exist)
    if project_folder == '':
        print('error: fail to create project.')
    else:
        print(f'create project successfully in {project_folder}.')
