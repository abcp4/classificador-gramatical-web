my_table = """
    <table>
        <thead>
            <tr>
                <th></th>
                <th><span style="font-weight:bold;">morfologia</span></th>
            </tr>
        </thead>
        <tbody>{body}</tbody>
    </table>
    """


def format_morph(morph):
    return "; ".join(
        f"<span style='font-weight:bold'>{category}</span>: {type}"
        for category, type in morph
    )


def create_tbody(tokens, frase_morph):

    return "\n".join(
        f"""
    <tr>
        <td><span style="font-weight:bold;">{tokens[index]}</span></td>
        <td>{format_morph(morph)}</td>
    </tr>
    """
        for index, morph in enumerate(frase_morph)
    )
