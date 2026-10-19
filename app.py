import os

from mcp.server import MCPServer


mcp = MCPServer("MCP Test Server")


@mcp.tool()
def saludar(nombre: str) -> str:
    """
    Devuelve un saludo personalizado.

    Args:
        nombre: Nombre de la persona que recibirá el saludo.
    """
    return f"Hola, {nombre}. El servidor MCP funciona correctamente."


@mcp.tool()
def comprobar_servidor() -> dict:
    """
    Comprueba el estado básico del servidor MCP.
    """
    return {
        "estado": "OK",
        "servidor": "MCP Test Server",
        "transporte": "Streamable HTTP"
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))

    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port
    )
    
