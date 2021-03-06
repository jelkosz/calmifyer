from common.constants import LABEL

def boldFormat(bold):
    return [{'userEnteredFormat': {'textFormat': {'bold': bold}}}]

def formatted_label_from_config(config):
    labelValue = config[LABEL]
    labelFormat = config.get(LABEL + '-format', None)

    if labelFormat is None:
        return labelValue
    else:
        return {'value': labelValue, 'format': labelFormat}