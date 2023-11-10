from xml.dom import ValidationErr


def validate_file_extension(file_extension, is_scraped_file: bool) -> None:
    required_extension = 'xls' if is_scraped_file else 'pdf'

    if file_extension != required_extension:
        raise ValidationErr(
            f'Only {required_extension.upper()} files are accepted for {"scraped data" if is_scraped_file else "parsing data"}.'
        )


validate_file_extension('doc', False)
