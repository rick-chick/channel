import os
import sys
import snakecase
from colorama import Fore, Style, init

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

init(autoreset=True)


def generate_file_from_template(
        template_file, model, action, destination_dir,
        device="", suffix="", need_input=True):
    template_content = ""
    with open(template_file, "r") as template:
        template_content = template.read()

        model_lower = snakecase.convert(model)
        action_lower = snakecase.convert(action)
        device_lower = snakecase.convert(device)

        content = template_content.format(
            model=model,
            model_lower=model_lower,
            action=action,
            action_lower=action_lower,
            device=device,
            device_lower=device_lower)

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        file_path: str
        action_str: str = ""
        if (action):
            action_str = f"_{action_lower}"
        if (not device):
            file_path = os.path.join(
                destination_dir,
                f"{model_lower}{action_str}{suffix}.py")
        else:
            file_path = os.path.join(
                destination_dir,
                f"{device_lower}_{model_lower}{action_str}{suffix}.py")

        if confirm_overwrite(file_path):
            with open(file_path, "w") as generated_file:
                generated_file.write(content)
            print((
                # Fore.GREEN,
                f"ファイル '{file_path}' が保存されました。",
                # Style.RESET_ALL
            ))

            init_file_path = os.path.join(destination_dir, "__init__.py")
            base_name = os.path.basename(file_path)
            file_name_without_extension = os.path.splitext(base_name)[0]

            line = f"{os.linesep}from .{file_name_without_extension} import *"
            if (need_input):
                with open(init_file_path, "a") as init_file:
                    init_file.write(line)
                print((
                    # Fore.GREEN,
                    f"ファイル '{init_file_path}' を更新しました",
                    # Style.RESET_ALL
                ))
        else:
            print((
                # Fore.RED,
                "ファイルの保存がキャンセルされました。",
                # Style.RESET_ALL
            ))


def confirm_overwrite(file_path):
    if os.path.exists(file_path):
        while True:
            response = input(
                f"ファイル '{file_path}' は既に存在します。上書きしてもよろしいですか？ (y/n): ")
            if response.lower() == "y":
                return True
            elif response.lower() == "n":
                return False
            else:
                print("y または n を入力してください。")
    return True


def file_path(file_name: str):
    return os.path.join(script_directory, file_name)


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate.py generate <command>")
        return

    if sys.argv[1] == "generate":
        command = sys.argv[2]
        if command == "usecase":
            generate_usecase()
        elif command == "gateway":
            generate_adapter_gateway()
        elif command == "presenter":
            generate_adapter_presenter()
        elif command == "repository":
            generate_driver_repository()
        elif command == "invoker":
            generate_driver_invoker()
        elif command == "controller":
            generate_adapter_controller()
        elif command == "handler":
            generate_driver_handler()
        elif command == "view":
            generate_driver_view()
        else:
            print("Unknown command:", command)
    else:
        print("Unknown command:", sys.argv[1])


def generate_usecase():

    # 他のファイルへの相対パスを生成
    model = input("Enter the model name by CamelCase: ")
    action = input("Enter the action name by CamelCase: ")

    model_lower = snakecase.convert(model)
    action_lower = snakecase.convert(action)

    action_path = ""
    if action in ["Create", "Update", "Delete", "List", "Get", "Upload"]:
        action_path = f"/{action_lower}"

    templates_dir = file_path(f"templates/src/usecase{action_path}")
    input_port_template = os.path.join(templates_dir, "input_port.txt")
    output_port_template = os.path.join(templates_dir, "output_port.txt")
    repository_template = os.path.join(templates_dir, "repository.txt")
    interactor_template = os.path.join(templates_dir, "interactor.txt")
    templates_test_dir = file_path(f"templates/tests/usecase{action_path}")
    interactor_test_template = os.path.join(
        templates_test_dir, "interactor.txt")

    project_dir = file_path("../src/channel/")
    input_port_dir = os.path.join(
        project_dir, f"usecase/input_port/{model_lower}")
    output_port_dir = os.path.join(
        project_dir, f"usecase/output_port/{model_lower}")
    repository_dir = os.path.join(
        project_dir, f"usecase/repository/{model_lower}")
    interactor_dir = os.path.join(
        project_dir, f"usecase/interactor/{model_lower}")

    test_dir = file_path("../tests/channel")
    interactor_test_dir = os.path.join(
        test_dir, f"usecase/interactor/{model_lower}")

    generate_file_from_template(
        input_port_template, model, action, input_port_dir,
        suffix="_input_port")
    generate_file_from_template(
        output_port_template, model, action, output_port_dir,
        suffix="_output_port")
    generate_file_from_template(
        repository_template, model, action, repository_dir,
        suffix="_repository")
    generate_file_from_template(
        interactor_template, model, action, interactor_dir,
        suffix="_interactor")
    generate_file_from_template(
        interactor_test_template, model, action, interactor_test_dir,
        suffix="_interactor_test", need_input=False)


def generate_adapter_gateway():

    # 他のファイルへの相対パスを生成
    model = input("Enter the model name by CamelCase: ")
    action = input("Enter the action name by CamelCase: ")

    model_lower = snakecase.convert(model)
    action_lower = snakecase.convert(action)

    action_path = ""
    if action in ["Create", "Update", "Delete", "List", "Get", "Upload"]:
        action_path = f"/{action_lower}"

    # templates(src)
    templates_dir = file_path(f"templates/src/adapter{action_path}")
    gateway_template = os.path.join(templates_dir, "gateway.txt")

    # templates(src/repository)
    gateway_repository_template = os.path.join(templates_dir, "repository.txt")

    # templates(tests)
    templates_test_dir = file_path(f"templates/tests/adapter{action_path}")
    gateway_test_template = os.path.join(
        templates_test_dir, "gateway.txt")

    # templates(tests/repository)
    gateway_test_repository_template = os.path.join(
        templates_test_dir, "repository_impl.txt")

    # out(src)
    project_dir = file_path("../src/channel/")
    gateway_dir = os.path.join(
        project_dir, f"adapter/gateway/{model_lower}")

    # out(src/repository)
    gateway_repository_dir = gateway_dir

    # out(tests)
    test_dir = file_path("../tests/channel")
    gateway_test_dir = os.path.join(
        test_dir, f"adapter/gateway/{model_lower}")

    gateway_test_repository_dir = gateway_test_dir

    # generate(src)
    generate_file_from_template(
        gateway_template, model, action, gateway_dir, suffix="_gateway")
    # generate(src/repository)
    generate_file_from_template(
        gateway_repository_template, model, "", gateway_repository_dir, suffix="_repository")
    # generate(tests)
    generate_file_from_template(
        gateway_test_template, model, action, gateway_test_dir,
        suffix="_gateway_test", need_input=False)
    # generate(tests/repository)
    generate_file_from_template(
        gateway_test_repository_template, model, "", gateway_test_repository_dir,
        suffix="_repository_impl", need_input=False)


def generate_adapter_controller():

    # 他のファイルへの相対パスを生成
    model = input("Enter the model name by CamelCase: ")
    action = input("Enter the action name by CamelCase: ")

    model_lower = snakecase.convert(model)
    action_lower = snakecase.convert(action)

    action_path = ""
    if action in ["Create", "Update", "Delete", "List", "Get", "Upload"]:
        action_path = f"/{action_lower}"

    # src template
    templates_dir = file_path(f"templates/src/adapter{action_path}")
    controller_template = os.path.join(templates_dir, "controller.txt")

    # tests template
    templates_test_dir = file_path(f"templates/tests/adapter{action_path}")
    controller_test_template = os.path.join(
        templates_test_dir, "controller.txt")

    # src 
    project_dir = file_path("../src/channel/")
    controller_dir = os.path.join(
        project_dir, f"adapter/controller/{model_lower}")

    # tests
    test_dir = file_path("../tests/channel")
    controller_test_dir = os.path.join(
        test_dir, f"adapter/controller/{model_lower}")

    generate_file_from_template(
        controller_template, model, action, controller_dir, suffix="_controller")
    generate_file_from_template(
        controller_test_template, model, action, controller_test_dir,
        suffix="_controller_test", need_input=False)
    generate_file_from_template(
        controller_template, model, action, controller_test_dir,
        suffix="_input_parser_impl", need_input=False)


def generate_adapter_presenter():

    # 他のファイルへの相対パスを生成
    model = input("Enter the model name by CamelCase: ")
    action = input("Enter the action name by CamelCase: ")

    model_lower = snakecase.convert(model)
    action_lower = snakecase.convert(action)

    action_path = ""
    if action in ["Create", "Update", "Delete", "List", "Get", "Upload"]:
        action_path = f"/{action_lower}"

    # templates(src)
    templates_dir = file_path(f"templates/src/adapter{action_path}")
    presenter_template = os.path.join(templates_dir, "presenter.txt")

    # templates(src/view)
    presenter_view_template = os.path.join(templates_dir, "view.txt")

    # template(tests)
    templates_test_dir = file_path(f"templates/tests/adapter{action_path}")
    presenter_test_template = os.path.join(
        templates_test_dir, "presenter.txt")

    # template(tests/view_impl)
    templates_test_view_dir = file_path(
        f"templates/tests/adapter{action_path}")
    presenter_test_view_impl_template = os.path.join(
        templates_test_view_dir, "view_impl.txt")

    # out pass (src)
    project_dir = file_path("../src/channel/")
    presenter_dir = os.path.join(
        project_dir, f"adapter/presenter/{model_lower}")

    # outs pass(view)
    presenter_view_impl_dir = os.path.join(
        project_dir, f"adapter/presenter/{model_lower}")

    # outs pass(tests)
    test_dir = file_path("../tests/channel")
    presenter_test_dir = os.path.join(
        test_dir, f"adapter/presenter/{model_lower}")

    # outs pass(tests/view_impl)
    presenter_test_view_impl_dir = os.path.join(
        test_dir, f"adapter/presenter/{model_lower}")

    # generate(src)
    generate_file_from_template(
        presenter_template, model, action, presenter_dir, suffix="_presenter")
    # generate(src/view)
    generate_file_from_template(
        presenter_view_template, model, action, presenter_dir, suffix="_view")
    # generate(tests)
    generate_file_from_template(
        presenter_test_template, model, action, presenter_test_dir,
        suffix="_presenter_test", need_input=False)
    # generate(tests/view_impl)
    generate_file_from_template(
        presenter_test_view_impl_template, model, action, presenter_test_view_impl_dir,
        suffix="_view_impl", need_input=False)


def generate_driver_repository():

    # 他のファイルへの相対パスを生成
    model = input("Enter the model name by CamelCase: ")
    action = ""
    device = input(
        "Enter the device name by CamelCase( like Sqlalchemy): ")

    #  model_lower = snakecase.convert(model)
    device_lower = snakecase.convert(device)

    templates_dir = file_path(
        f"templates/src/driver/db/{device_lower}/")
    repository_template = os.path.join(templates_dir, "repository.txt")
    templates_test_dir = file_path(
        f"templates/tests/driver/db/{device_lower}/")
    repository_test_template = os.path.join(
        templates_test_dir, "repository.txt")

    project_dir = file_path("../src/channel/")
    repository_dir = os.path.join(
        project_dir,
        f"driver/db/{device_lower}")

    test_dir = file_path("../tests/channel")
    repository_test_dir = os.path.join(
        test_dir,
        f"driver/db/{device_lower}")

    generate_file_from_template(
        repository_template, model, action, repository_dir,
        suffix="_repository", device=device)
    generate_file_from_template(
        repository_test_template, model, action, repository_test_dir,
        suffix="_repository_test", device=device, need_input=False)


def generate_driver_invoker():

    # 他のファイルへの相対パスを生成
    model = input("Enter the model name by CamelCase: ")
    action = input("Enter the action name by CamelCalse: ")
    device = input(
        "Enter the device name by CamelCase( like Cli): ")

    #  model_lower = snakecase.convert(model)
    device_lower = snakecase.convert(device)
    model_lower = snakecase.convert(model)
    action_lower = snakecase.convert(action)

    action_path = ""
    if action in ["Create", "Update", "Delete", "List", "Get", "Upload"]:
        action_path = f"/{action_lower}"

    templates_dir = file_path(
        f"templates/src/driver/{device_lower}{action_path}/")
    invoker_template = os.path.join(templates_dir, "invoker.txt")
    templates_test_dir = file_path(
        f"templates/tests/driver/{device_lower}{action_path}/")
    invoker_test_template = os.path.join(
        templates_test_dir, "invoker.txt")

    project_dir = file_path("../src/channel/")
    invoker_dir = os.path.join(
        project_dir,
        f"driver/{device_lower}/invokers/{model_lower}")

    test_dir = file_path("../tests/channel")
    invoker_test_dir = os.path.join(
        test_dir,
        f"driver/{device_lower}/invokers/{model_lower}")

    generate_file_from_template(
        invoker_template, model, action, invoker_dir,
        suffix="_invoker", device=device)
    generate_file_from_template(
        invoker_test_template, model, action, invoker_test_dir,
        suffix="_invoker_test", device=device, need_input=False)


def generate_driver_handler():

    # 他のファイルへの相対パスを生成
    model = input("Enter the model name by CamelCase: ")
    action = input("Enter the action name by CamelCalse: ")
    device = input(
        "Enter the device name by CamelCase( like Cli): ")

    #  model_lower = snakecase.convert(model)
    device_lower = snakecase.convert(device)
    model_lower = snakecase.convert(model)
    action_lower = snakecase.convert(action)

    action_path = ""
    if action in ["Create", "Update", "Delete", "List", "Get", "Upload"]:
        action_path = f"/{action_lower}"

    # template(src)
    templates_dir = file_path(
        f"templates/src/driver/handler/{device_lower}{action_path}"
    )
    handler_template = os.path.join(templates_dir, "handler.txt")
    # template(src/parser)
    handler_parser_template = os.path.join(templates_dir, "parser.txt")

    # template(tests)
    templates_test_dir = file_path(
        f"templates/tests/driver/handler/{device_lower}/{action_path}/")
    handler_test_template = os.path.join(
        templates_test_dir, "handler.txt")
    # src
    project_dir = file_path("../src/channel/")
    handler_dir = os.path.join(
        project_dir,
        (
            f"driver/handler/{device_lower}/{model_lower}/"
        )
    )
    # src/parser
    handler_parser_dir = os.path.join(
        project_dir,
        (
            f"driver/handler/{device_lower}/{model_lower}/"
        )
    )
    # tests
    test_dir = file_path("../tests/channel")
    handler_test_dir = os.path.join(
        test_dir,
        (
            f"driver/handler/{device_lower}/{model_lower}/"
        )
    )
    generate_file_from_template(
        handler_parser_template, model, action, handler_parser_dir,
        suffix="_input_parser", device=device)
    generate_file_from_template(
        handler_template, model, action, handler_dir,
        suffix="_handler", device=device,  need_input=False)
    generate_file_from_template(
        handler_test_template, model, action, handler_test_dir,
        suffix="_handler_test", device=device, need_input=False)


def generate_driver_view():

    # 他のファイルへの相対パスを生成
    model = input("Enter the model name by CamelCase: ")
    action = input("Enter the action name by CamelCalse: ")
    device = input(
        "Enter the device name by CamelCase( like Cli): ")

    #  model_lower = snakecase.convert(model)
    device_lower = snakecase.convert(device)
    model_lower = snakecase.convert(model)
    action_lower = snakecase.convert(action)

    action_path = ""
    if action in ["Create", "Update", "Delete", "List", "Get", "Upload"]:
        action_path = f"/{action_lower}"
    else:
        print("unimplemented action")

    # template(src)
    templates_dir = file_path(
        f"templates/src/driver/view/{device_lower}/{action_path}"
    )
    view_template = os.path.join(templates_dir, "view.txt")
    # template(tests)
    templates_test_dir = file_path(
        f"templates/tests/driver/view/{device_lower}/{action_path}/")
    view_test_template = os.path.join(
        templates_test_dir, "view.txt")
    # src
    project_dir = file_path("../src/channel/")
    view_dir = os.path.join(
        project_dir,
        f"driver/view/{device_lower}/{model_lower}/"
    )
    # tests
    test_dir = file_path("../tests/channel")
    view_test_dir = os.path.join(
        test_dir,
        f"driver/view/{device_lower}/{model_lower}/"
    )
    # generate template
    generate_file_from_template(
        view_template, model, action, view_dir,
        suffix="_view", device=device)
    generate_file_from_template(
        view_test_template, model, action, view_test_dir,
        suffix="_view_test", device=device, need_input=False)
    generate_file_from_template(
        view_test_template, model, action, view_test_dir,
        suffix="_view_test", device=device, need_input=False)


if __name__ == "__main__":
    main()
