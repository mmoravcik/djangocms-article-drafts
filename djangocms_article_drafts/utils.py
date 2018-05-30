def get_fields_to_copy(obj, exclude_fields=None):
    """
    This has been copied from https://github.com/divio/djangocms-publisher
    """
    all_exclude_fields = set(['pk', 'id'])
    if exclude_fields:
        all_exclude_fields |= set(exclude_fields)

    fields = {}
    for field in obj._meta._get_fields(forward=True, reverse=False):
        if (
            not field.concrete or
            field.auto_created or
            field.name in all_exclude_fields
        ):
            continue
        elif (
            field.is_relation and
            (field.one_to_one or field.many_to_many or field.one_to_many)
        ):
            # Can't copy a OneToOne, it'll cause a unique constraint error.
            # many_to_many are up to the user.
            # one_to_many are up to the user.
            continue
        else:
            # Non-relation fields.
            # many_to_one: ForeignKeys to other models
            fields[field.name] = getattr(obj, field.name)
    return fields


def copy_object(old_obj, new_obj, exclude_fields=None, extra_values=None):
    """
    This has been copied from https://github.com/divio/djangocms-publisher
    """
    extra_values = extra_values or {}
    fields_to_copy = get_fields_to_copy(old_obj, exclude_fields=exclude_fields)
    fields_to_copy.update(extra_values)
    for name, value in fields_to_copy.items():
        setattr(new_obj, name, value)
