from i3ipc import Connection

i3 = Connection()

EXCLUDED_OUTPUTS = ["__i3"]


def append_string_to_workspaces(append_string, workspace_counter, workspace_name):
    """Rename the given workspace by appending a string to the workspace name."""
    rename_workspace(workspace_name, f"{workspace_name}{append_string}")
    workspace_counter += 1
    return workspace_counter


def get_outputs():
    """Get the available outputs, excluding outputs in the EXCLUDED_OUTPUTS variable."""
    outputs = []
    tree = i3.get_tree()
    for node in filter(
        lambda node: node.type == "output" and node.name not in EXCLUDED_OUTPUTS, tree
    ):
        workspaces = node.nodes[1].nodes
        if workspaces:
            outputs.append((node, workspaces))
    return outputs


def rename_workspace(original_workspace_name, new_workspace_name):
    """Rename a workspace."""
    i3.command(
        f'rename workspace "{original_workspace_name}" to "{new_workspace_name}"'
    )


def rename_workspaces(append_string, function, outputs):
    """Iterate over the workspaces and rename them."""
    workspace_counter = 1
    for output in outputs:
        for workspace in output[1]:
            workspace_name = workspace.name
            workspace_counter = function(
                append_string, workspace_counter, workspace_name
            )


def reset_renamed_workspaces(append_string, workspace_counter, workspace_name):
    """Rename the given workspace according to its numbered position (from left to right, across outputs)."""
    rename_workspace(f"{workspace_name}{append_string}", workspace_counter)
    workspace_counter += 1
    return workspace_counter


def reset_workspaces(append_string, outputs):
    """See append_string_to_workspaces and reset_renamed_workspaces functions for more information."""
    rename_workspaces(append_string, append_string_to_workspaces, outputs)
    rename_workspaces(append_string, reset_renamed_workspaces, outputs)


outputs = get_outputs()

# Sort outputs by position, from left to right
outputs.sort(key=lambda output: output[0].rect.x)

reset_workspaces("...", outputs)
