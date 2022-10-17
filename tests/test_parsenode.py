from nibv.generator.axonparser import parse_signature


def test_parsenode():
    signature = "\
signature = Signature(\
'read', ReadDiskItem('Sulci Segments Model', 'Text data table'),\
'levels', Choice((_t_('1: High probability (70% rejected)'), 1),\
                    (_t_('2: Intermediate probability (40% rejected)'), 2),\
                    (_t_('3: Low probability (20% rejected)'), 4),\
                    (_t_('1-2: High-inter probabilities'), 3),\
                    (_t_('1-3: All 3 probabilities thesholds'), 7)),\
'show_unknown', Boolean(),\
'nomenclature', ReadDiskItem('Nomenclature', 'Hierarchy'),\
'show_mesh', Boolean(),\
'white_mesh', ReadDiskItem('White SPAM mesh', 'anatomist mesh formats'),\
'mesh_TO_spam', ReadDiskItem('Transformation', 'Transformation Matrix'),\
)"
    traits = parse_signature(signature)

    assert traits['read']['type'] == "ReadDiskItem"
    assert len(traits) == 7
    assert len(traits['levels']['values']) == 5
    assert int(traits['levels']['values'][4][0]) == 7


if __name__ == "__main__":
    test_parsenode()
