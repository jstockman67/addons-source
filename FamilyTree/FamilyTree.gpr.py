register(REPORT,
    id = 'FamilyTree',
    name = _('Family Tree'),
    description = _('Produces a graphical family tree.'),
    version = '4.2.10',
    gramps_target_version = "5.0",
    status = STABLE,
    fname = 'FamilyTree.py',
    reportclass = 'FamilyTree',
    optionclass = 'FamilyTreeOptions',
    authors = ['Reinhard Mueller'],
    authors_email = ['reinhard.mueller@igal.at'],
    category = CATEGORY_DRAW,
    report_modes = [REPORT_MODE_GUI, REPORT_MODE_CLI]
    )
