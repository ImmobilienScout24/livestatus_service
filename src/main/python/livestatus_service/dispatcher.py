from livestatus_service.livestatus import perform_query as perform_livestatus_query
from livestatus_service.livestatus import perform_command as perform_livestatus_command
from livestatus_service.configuration import get_current_configuration


def perform_query(query, key=None, handler=None):
    if handler is None or handler == 'livestatus':
        socket_path = get_current_configuration().livestatus_socket

        return perform_livestatus_query(query, socket_path, key)
    else:
        return None


def perform_command(command, key=None, handler=None):
    if handler is None or handler == 'livestatus':
        socket_path = get_current_configuration().livestatus_socket

        return perform_livestatus_command(command, socket_path, key)
    else:
        return None
