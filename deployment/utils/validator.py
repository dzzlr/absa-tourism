class Validator:
    MESSAGE = []

    def __init__(self, text: str, validation_rules: str):
        self.text = text
        self.validation_rules = validation_rules.split('|')
        self.validate = self.validate(self.text, self.validation_rules)

    def validate(self, text:str, validation_rules: list):
        for rule in validation_rules:
            if 'required' == rule:
                if len(text) == 0:
                    self.MESSAGE.append('must not be blank')
            if 'min:' in rule[:-1]:
                min_rule = rule.split(':')
                if len(text) <= int(min_rule[1]):
                    self.MESSAGE.append(f'must be greater than {min_rule[1]} characters')
            if 'max:' in rule:
                max_rule = rule.split(':')
                if len(text) >= int(max_rule[1]):
                    self.MESSAGE.append(f'must be less than {max_rule[1]} characters')
    
        return self.MESSAGE
    
    def getText(self):
        return self.text
    
    def getValidationRules(self):
        return self.validation_rules
    
    def getMessage(self):
        if len(self.MESSAGE) != 0:
            message = {'code': 400, 'status': 'BAD_REQUEST', 'errors': [self.MESSAGE]}
        else:
            message = {'code': 200, 'status': 'OK', 'text': self.getText()}
        return message

if __name__ == "__main__":
    validatedData = Validator("","required|min:2|max:100")
    # print(validatedData.getText())
    # print(validatedData.getMessage()['code'] == 400)