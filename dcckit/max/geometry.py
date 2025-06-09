import Autodesk.Max
import numpy as np
from dcckit.max.sdk import inode


def get_verts(node):
    """
    Gets the vertices for the input object as a numpy array

    Args:
        node (rt.Node): The node to get the vertices from
    Returns:
        numpy.ndarray: The vertices for the input object
    """
    try:
        sdk_node = inode.find_with_handle(node.inode.handle)
        world_state = sdk_node.EvalWorldState(0, False)
        obj = world_state.Obj.__implementation__
        output = None

        if isinstance(obj, Autodesk.Max.Wrappers.PolyObject):
            mesh = obj.Mesh

            num_verts = mesh.VNum
            output = np.zeros((num_verts, 3), dtype=np.float32)

            for i in range(mesh.VNum):
                pos = mesh.V(i).P
                x, y, z = pos.X, pos.Y, pos.Z
                output[i] = np.array([x, y, z], dtype=np.float32)

        elif isinstance(obj, Autodesk.Max.Wrappers.TriObject):
            mesh = obj.Mesh_

            num_verts = mesh.NumVerts
            output = np.zeros((num_verts, 3), dtype=np.float32)

            def get_vert(i):
                pos = mesh.GetVert(i)
                x, y, z = pos.X, pos.Y, pos.Z
                return np.array([x, y, z], dtype=np.float32)

            num_verts = mesh.NumVerts
            output = np.zeros((num_verts, 3), dtype=np.float32)

            for i in range(mesh.NumVerts):
                pos = mesh.GetVert(i)
                x, y, z = pos.X, pos.Y, pos.Z
                output[i] = np.array([x, y, z], dtype=np.float32)

        return output

    except Exception as e:
        raise e
        # Not a geometry type
        # Note: It's quicker here to just try and catch the exception
        # than to run any validation checks
        return None


def get_tri_count(*args):
    """
    Gets the number of tris for the input objects

    Note: The number of internal tris (not polys)

    Args:
        *args: The nodes to get the tri count from
    """
    output = 0

    sdk_nodes = [inode.find_with_handle(node.inode.handle) for node in args]

    for sdk_node in sdk_nodes:
        try:
            world_state = sdk_node.EvalWorldState(0, False)
            obj = world_state.Obj.__implementation__

            if isinstance(obj, Autodesk.Max.Wrappers.PolyObject):
                mesh = obj.Mesh
                output += mesh.TriNum

            elif isinstance(obj, Autodesk.Max.Wrappers.TriObject):
                mesh = obj.Mesh_
                output += mesh.NumFaces
        except Exception:
            pass

    return output
