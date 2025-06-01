

def make_prompt(inputs:dict, prompt_type:str = None):
    if prompt_type == 'zero_shot':
        return """Suggest one critical question that directly challenges an argument in this text:
<text>
{intervention}
</text>

Requirements for the question:
<requirement>
1. Keep the question simple—no explanations or justifications.
2. Ensure logical reasoning aligns with the text.
3. Focus exclusively on content within the provided text.
4. Avoid introducing new concepts or external ideas.
5. Make it specific to the arguments in the text (not generic).
6. Target a single argument critically (e.g., a precise reading-comprehension critique).
</requirement>
""".format_map(inputs)


    elif prompt_type == 'requirements_ahead':
        return """Suggest one critical question that directly challenges an argument in the given text.

Requirements for the question:
<requirement>
1. Be useful (challenge one of the arguments in the text).
2. The reasoning should be right.
3. Be related to the text.
4. Do not introduce new concepts not present in the text.
5. Avoid being too general that could be applied to any text.
6. Be critical with one of the argument in the text (e.g. a reading-comprehension question).
</requirement>

Here is an example.
<text>
travellots: "There should be no discrimination in how a passenger is bumped or compensated just because they may have paid less for a ticket or used frequent flyer miles.\nAirline tickets are not lottery tickets.\nOne does not purchase a ticket hoping to reach a certain destination.\nSame as if one pays $4 for a cup of coffee or $1, the cup is supposed to have coffee in it.\nThe price does not dictate that "maybe" you will get the product or service.\nAlso, the airline decides what prices or miles are used to purchase a promise to get you from point A to point B.\nIf they can not afford to give  a ticket for that price, they should not sell it.\nWhen you reserve a ticket, the assumption is that you will be taken from point A to point B by the times given by the airline.\nA passenger does not purchase a ticket just to see if maybe they can get somewhere because they have nothing better to do."
</text>

Useful questions:
"Is it fair to compare airline tickets to cups of coffee, given that airline travel involves complex logistical and safety considerations that may not be applicable to other consumer products?"
"Is it fair to assume that the airline is making a promise to get the passenger from point A to point B, or are there circumstances in which the airline cannot fulfill this promise?"
"Are there any circumstances under which an airline might need to bump a passenger, such as in cases of overbooking or mechanical issues, and how should these situations be handled?"
"Is it reasonable to expect that the airline can always accommodate all passengers, or are there situations in which bumping passengers is necessary?"
"Is the analogy between airline tickets and coffee cups a good one, or are there important differences between the two?"
"Are there any differences between purchasing a ticket with cash versus frequent flyer miles that might affect the passenger's rights or expectations?"
"Is the argument assuming that the only factor that determines the price of an airline ticket is the airline's costs, or are there other factors at play?"
"Could not discriminating passengers in how they are compensated just because they may have paid less for a ticket have consequences that we should take into account? Is it practically possible?"
"Are there any exceptions to the principle of non-discrimination in bumping or compensation, such as in cases of emergency or special circumstances?"
"Are there any circumstances in which the airline might need to prioritize certain passengers over others?"


Unhelpful questions:
"How do airlines determine the prices of their tickets, and are these prices transparent to consumers?"
"What happens when an airline sells a ticket at a price that is lower than its actual cost, and how does this impact the airline's ability to provide the promised service?"
"How does the assumption that a passenger will be taken from point A to point B by the times given by the airline account for unexpected disruptions or changes in flight schedules?"
"Are there alternative actions to not discriminating passengers in how they are compensated just because they may have paid less for a ticket to achieve receiving a product you have paid for? If so, which is the most efficient action?"
"What are the critical questions that should be asked regarding the arguments in this paragraph?"
"How do airlines currently handle bumping and compensation, and are there any existing regulations or industry standards that govern these practices?"
"Are there other relevant goals that conflict with receiving a product you have paid for?"
"What critical questions should be raised before accepting the arguments in this text?"

<text>
{intervention}
</text>

Please give an useful question.
""".format_map(inputs)


    elif prompt_type == 'oral_expression':
        return """Suggest one critical question that directly challenges an argument in this text:
<text>
{intervention}
</text>

Requirements for the question:
<requirement>
1. Be useful (challenge one of the arguments in the text).
2. The reasoning should be right.
3. Be related to the text.
4. Do not introduce new concepts not present in the text.
5. Avoid being too general that could be applied to any text.
6. Be critical with one of the argument in the text (e.g. a reading-comprehension question).
</requirement>

Here is an example.
<text>
travellots: "There should be no discrimination in how a passenger is bumped or compensated just because they may have paid less for a ticket or used frequent flyer miles.\nAirline tickets are not lottery tickets.\nOne does not purchase a ticket hoping to reach a certain destination.\nSame as if one pays $4 for a cup of coffee or $1, the cup is supposed to have coffee in it.\nThe price does not dictate that "maybe" you will get the product or service.\nAlso, the airline decides what prices or miles are used to purchase a promise to get you from point A to point B.\nIf they can not afford to give  a ticket for that price, they should not sell it.\nWhen you reserve a ticket, the assumption is that you will be taken from point A to point B by the times given by the airline.\nA passenger does not purchase a ticket just to see if maybe they can get somewhere because they have nothing better to do."
</text>

Useful questions:
"Is it fair to compare airline tickets to cups of coffee, given that airline travel involves complex logistical and safety considerations that may not be applicable to other consumer products?"
"Is it fair to assume that the airline is making a promise to get the passenger from point A to point B, or are there circumstances in which the airline cannot fulfill this promise?"
"Are there any circumstances under which an airline might need to bump a passenger, such as in cases of overbooking or mechanical issues, and how should these situations be handled?"
"Is it reasonable to expect that the airline can always accommodate all passengers, or are there situations in which bumping passengers is necessary?"
"Is the analogy between airline tickets and coffee cups a good one, or are there important differences between the two?"
"Are there any differences between purchasing a ticket with cash versus frequent flyer miles that might affect the passenger's rights or expectations?"
"Is the argument assuming that the only factor that determines the price of an airline ticket is the airline's costs, or are there other factors at play?"
"Could not discriminating passengers in how they are compensated just because they may have paid less for a ticket have consequences that we should take into account? Is it practically possible?"
"Are there any exceptions to the principle of non-discrimination in bumping or compensation, such as in cases of emergency or special circumstances?"
"Are there any circumstances in which the airline might need to prioritize certain passengers over others?"


Unhelpful questions:
"How do airlines determine the prices of their tickets, and are these prices transparent to consumers?"
"What happens when an airline sells a ticket at a price that is lower than its actual cost, and how does this impact the airline's ability to provide the promised service?"
"How does the assumption that a passenger will be taken from point A to point B by the times given by the airline account for unexpected disruptions or changes in flight schedules?"
"Are there alternative actions to not discriminating passengers in how they are compensated just because they may have paid less for a ticket to achieve receiving a product you have paid for? If so, which is the most efficient action?"
"What are the critical questions that should be asked regarding the arguments in this paragraph?"
"How do airlines currently handle bumping and compensation, and are there any existing regulations or industry standards that govern these practices?"
"Are there other relevant goals that conflict with receiving a product you have paid for?"
"What critical questions should be raised before accepting the arguments in this text?"

Please give an useful question.
""".format_map(inputs)


    elif prompt_type == 'few_shot':
        return """Suggest one critical question that directly challenges an argument in this text:
<text>
{intervention}
</text>

Requirements for the question:
<requirement>
1. Keep the question simple—no explanations or justifications.
2. Ensure logical reasoning aligns with the text.
3. Focus exclusively on content within the provided text.
4. Avoid introducing new concepts or external ideas.
5. Make it specific to the arguments in the text (not generic).
6. Target a single argument critically (e.g., a precise reading-comprehension critique).
</requirement>

Here is an example.
<text>
travellots: "There should be no discrimination in how a passenger is bumped or compensated just because they may have paid less for a ticket or used frequent flyer miles.\nAirline tickets are not lottery tickets.\nOne does not purchase a ticket hoping to reach a certain destination.\nSame as if one pays $4 for a cup of coffee or $1, the cup is supposed to have coffee in it.\nThe price does not dictate that "maybe" you will get the product or service.\nAlso, the airline decides what prices or miles are used to purchase a promise to get you from point A to point B.\nIf they can not afford to give  a ticket for that price, they should not sell it.\nWhen you reserve a ticket, the assumption is that you will be taken from point A to point B by the times given by the airline.\nA passenger does not purchase a ticket just to see if maybe they can get somewhere because they have nothing better to do."
</text>

Useful questions:
"Is it fair to compare airline tickets to cups of coffee, given that airline travel involves complex logistical and safety considerations that may not be applicable to other consumer products?"
"Is it fair to assume that the airline is making a promise to get the passenger from point A to point B, or are there circumstances in which the airline cannot fulfill this promise?"
"Are there any circumstances under which an airline might need to bump a passenger, such as in cases of overbooking or mechanical issues, and how should these situations be handled?"
"Is it reasonable to expect that the airline can always accommodate all passengers, or are there situations in which bumping passengers is necessary?"
"Is the analogy between airline tickets and coffee cups a good one, or are there important differences between the two?"
"Are there any differences between purchasing a ticket with cash versus frequent flyer miles that might affect the passenger's rights or expectations?"
"Is the argument assuming that the only factor that determines the price of an airline ticket is the airline's costs, or are there other factors at play?"
"Could not discriminating passengers in how they are compensated just because they may have paid less for a ticket have consequences that we should take into account? Is it practically possible?"
"Are there any exceptions to the principle of non-discrimination in bumping or compensation, such as in cases of emergency or special circumstances?"
"Are there any circumstances in which the airline might need to prioritize certain passengers over others?"


Unhelpful questions:
"How do airlines determine the prices of their tickets, and are these prices transparent to consumers?"
"What happens when an airline sells a ticket at a price that is lower than its actual cost, and how does this impact the airline's ability to provide the promised service?"
"How does the assumption that a passenger will be taken from point A to point B by the times given by the airline account for unexpected disruptions or changes in flight schedules?"
"Are there alternative actions to not discriminating passengers in how they are compensated just because they may have paid less for a ticket to achieve receiving a product you have paid for? If so, which is the most efficient action?"
"What are the critical questions that should be asked regarding the arguments in this paragraph?"
"How do airlines currently handle bumping and compensation, and are there any existing regulations or industry standards that govern these practices?"
"Are there other relevant goals that conflict with receiving a product you have paid for?"
"What critical questions should be raised before accepting the arguments in this text?"

Please give an useful question.
""".format_map(inputs)


    elif prompt_type == 'sequential_2':
        return """Suggest one critical question that directly challenges an argument in the given text.

Requirements for the question:
<requirement>
1. Be useful (challenge one of the arguments in the text).
2. The reasoning should be right.
3. Be related to the text.
4. Do not introduce new concepts not present in the text.
5. Avoid being too general that could be applied to any text.
6. Be critical with one of the argument in the text (e.g. a reading-comprehension question).
</requirement>

Here is an example.
<text>
travellots: "There should be no discrimination in how a passenger is bumped or compensated just because they may have paid less for a ticket or used frequent flyer miles.\nAirline tickets are not lottery tickets.\nOne does not purchase a ticket hoping to reach a certain destination.\nSame as if one pays $4 for a cup of coffee or $1, the cup is supposed to have coffee in it.\nThe price does not dictate that "maybe" you will get the product or service.\nAlso, the airline decides what prices or miles are used to purchase a promise to get you from point A to point B.\nIf they can not afford to give  a ticket for that price, they should not sell it.\nWhen you reserve a ticket, the assumption is that you will be taken from point A to point B by the times given by the airline.\nA passenger does not purchase a ticket just to see if maybe they can get somewhere because they have nothing better to do."
</text>

Useful questions:
"Is it fair to compare airline tickets to cups of coffee, given that airline travel involves complex logistical and safety considerations that may not be applicable to other consumer products?"
"Is it fair to assume that the airline is making a promise to get the passenger from point A to point B, or are there circumstances in which the airline cannot fulfill this promise?"
"Are there any circumstances under which an airline might need to bump a passenger, such as in cases of overbooking or mechanical issues, and how should these situations be handled?"
"Is it reasonable to expect that the airline can always accommodate all passengers, or are there situations in which bumping passengers is necessary?"
"Is the analogy between airline tickets and coffee cups a good one, or are there important differences between the two?"
"Are there any differences between purchasing a ticket with cash versus frequent flyer miles that might affect the passenger's rights or expectations?"
"Is the argument assuming that the only factor that determines the price of an airline ticket is the airline's costs, or are there other factors at play?"
"Could not discriminating passengers in how they are compensated just because they may have paid less for a ticket have consequences that we should take into account? Is it practically possible?"
"Are there any exceptions to the principle of non-discrimination in bumping or compensation, such as in cases of emergency or special circumstances?"
"Are there any circumstances in which the airline might need to prioritize certain passengers over others?"


Unhelpful questions:
"How do airlines determine the prices of their tickets, and are these prices transparent to consumers?"
"What happens when an airline sells a ticket at a price that is lower than its actual cost, and how does this impact the airline's ability to provide the promised service?"
"How does the assumption that a passenger will be taken from point A to point B by the times given by the airline account for unexpected disruptions or changes in flight schedules?"
"Are there alternative actions to not discriminating passengers in how they are compensated just because they may have paid less for a ticket to achieve receiving a product you have paid for? If so, which is the most efficient action?"
"What are the critical questions that should be asked regarding the arguments in this paragraph?"
"How do airlines currently handle bumping and compensation, and are there any existing regulations or industry standards that govern these practices?"
"Are there other relevant goals that conflict with receiving a product you have paid for?"
"What critical questions should be raised before accepting the arguments in this text?"

<text>
{intervention}
</text>

Useful questions:
{cq}

Please give another useful question.
""".format(intervention=inputs['intervention'],cq=inputs['cqs'][0]['cq'])


    elif prompt_type == 'sequential_3':
        return """Suggest one critical question that directly challenges an argument in the given text.

Requirements for the question:
<requirement>
1. Be useful (challenge one of the arguments in the text).
2. The reasoning should be right.
3. Be related to the text.
4. Do not introduce new concepts not present in the text.
5. Avoid being too general that could be applied to any text.
6. Be critical with one of the argument in the text (e.g. a reading-comprehension question).
</requirement>

Here is an example.
<text>
travellots: "There should be no discrimination in how a passenger is bumped or compensated just because they may have paid less for a ticket or used frequent flyer miles.\nAirline tickets are not lottery tickets.\nOne does not purchase a ticket hoping to reach a certain destination.\nSame as if one pays $4 for a cup of coffee or $1, the cup is supposed to have coffee in it.\nThe price does not dictate that "maybe" you will get the product or service.\nAlso, the airline decides what prices or miles are used to purchase a promise to get you from point A to point B.\nIf they can not afford to give  a ticket for that price, they should not sell it.\nWhen you reserve a ticket, the assumption is that you will be taken from point A to point B by the times given by the airline.\nA passenger does not purchase a ticket just to see if maybe they can get somewhere because they have nothing better to do."
</text>

Useful questions:
"Is it fair to compare airline tickets to cups of coffee, given that airline travel involves complex logistical and safety considerations that may not be applicable to other consumer products?"
"Is it fair to assume that the airline is making a promise to get the passenger from point A to point B, or are there circumstances in which the airline cannot fulfill this promise?"
"Are there any circumstances under which an airline might need to bump a passenger, such as in cases of overbooking or mechanical issues, and how should these situations be handled?"
"Is it reasonable to expect that the airline can always accommodate all passengers, or are there situations in which bumping passengers is necessary?"
"Is the analogy between airline tickets and coffee cups a good one, or are there important differences between the two?"
"Are there any differences between purchasing a ticket with cash versus frequent flyer miles that might affect the passenger's rights or expectations?"
"Is the argument assuming that the only factor that determines the price of an airline ticket is the airline's costs, or are there other factors at play?"
"Could not discriminating passengers in how they are compensated just because they may have paid less for a ticket have consequences that we should take into account? Is it practically possible?"
"Are there any exceptions to the principle of non-discrimination in bumping or compensation, such as in cases of emergency or special circumstances?"
"Are there any circumstances in which the airline might need to prioritize certain passengers over others?"


Unhelpful questions:
"How do airlines determine the prices of their tickets, and are these prices transparent to consumers?"
"What happens when an airline sells a ticket at a price that is lower than its actual cost, and how does this impact the airline's ability to provide the promised service?"
"How does the assumption that a passenger will be taken from point A to point B by the times given by the airline account for unexpected disruptions or changes in flight schedules?"
"Are there alternative actions to not discriminating passengers in how they are compensated just because they may have paid less for a ticket to achieve receiving a product you have paid for? If so, which is the most efficient action?"
"What are the critical questions that should be asked regarding the arguments in this paragraph?"
"How do airlines currently handle bumping and compensation, and are there any existing regulations or industry standards that govern these practices?"
"Are there other relevant goals that conflict with receiving a product you have paid for?"
"What critical questions should be raised before accepting the arguments in this text?"

<text>
{intervention}
</text>

Useful questions:
{cq}
{cq2}

Please give another useful question.
""".format(intervention=inputs['intervention'],cq=inputs['cqs'][0]['cq'],cq2=inputs['cqs'][1]['cq'])


    else:
        raise ValueError(f'incorrect prompt_type:{prompt_type}')