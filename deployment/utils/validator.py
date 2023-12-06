class Validator:
    def __init__(self, text: str, validation_rules: str):
        self.text = text
        self.messages = []
        self.validation_rules = validation_rules.split('|')
        self.validate = self.validate(self.text, self.validation_rules)

    def validate(self, text:str, validation_rules: list):
        for rule in validation_rules:
            if 'required' == rule:
                if len(text) == 0:
                    self.setMessage('must not be blank')
            if 'min:' in rule[:-1]:
                min_rule = rule.split(':')
                if len(text) <= int(min_rule[1]):
                    self.setMessage(f'must be greater than {min_rule[1]} characters')
            if 'max:' in rule:
                max_rule = rule.split(':')
                if len(text) >= int(max_rule[1]):
                    self.setMessage(f'must be less than {max_rule[1]} characters')
    
    def getText(self):
        return self.text
    
    def getValidationRules(self):
        return self.validation_rules
    
    def setMessage(self, message):
        self.messages.append(message)
    
    def getMessage(self):
        if len(self.messages) != 0:
            messages = {'code': 400, 'status': 'BAD_REQUEST', 'errors': self.messages}
        else:
            messages = {'code': 200, 'status': 'OK', 'text': self.getText()}
        return messages

if __name__ == "__main__":
    validatedData = Validator("","required|min:2|max:100")
    # print(validatedData.getText())
    # print(validatedData.getMessage())
    # print(validatedData.getMessage()['code'] == 400)