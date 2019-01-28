import strcase

def check_cases(cases, func, *args):
    for inp, out in cases.items():
        assert func(inp, *args) == out

def test_to_camel():
    cases = {
        "test_case": "TestCase",
		"test": "Test",
		"TestCase":"TestCase",
		" test  case ": "TestCase",
		"": "",
		"many_many_words": "ManyManyWords",
		"AnyKind of_string": "AnyKindOfString",
		"odd-fix": "OddFix",
		"numbers2And55with000": "Numbers2And55With000"
    }
    check_cases(cases, strcase.to_camel)

def test_to_lower_camel():
    cases = {
        "foo-bar": "fooBar",
        "TestCase": "testCase",
        "": "",
        "AnyKind of_string": "anyKindOfString"
    }
    check_cases(cases, strcase.to_lower_camel)

def test_to_snake():
    cases = {
        "testCase": "test_case",
		"TestCase": "test_case",
		"Test Case": "test_case",
		" Test Case": "test_case",
		"Test Case ": "test_case",
		" Test Case ": "test_case",
		"test": "test",
		"test_case": "test_case",
		"Test": "test",
		"": "",
		"ManyManyWords": "many_many_words",
		"manyManyWords": "many_many_words",
		"AnyKind of_string": "any_kind_of_string",
		"numbers2and55with000": "numbers_2_and_55_with_000",
		"JSONData": "json_data",
		"userID": "user_id",
		"AAAbbb": "aa_abbb",
    }
    check_cases(cases, strcase.to_snake)

def test_to_delimited():
    cases = {
        "testCase": "test@case",
		"TestCase": "test@case",
		"Test Case": "test@case",
		" Test Case": "test@case",
		"Test Case ": "test@case",
		" Test Case ": "test@case",
		"test": "test",
		"test_case": "test@case",
		"Test": "test",
		"": "",
		"ManyManyWords": "many@many@words",
		"manyManyWords": "many@many@words",
		"AnyKind of_string": "any@kind@of@string",
		"numbers2and55with000": "numbers@2@and@55@with@000",
		"JSONData": "json@data",
		"userID": "user@id",
		"AAAbbb": "aa@abbb",
		"test-case": "test@case",
    }
    check_cases(cases, strcase.to_delimited, '@')

def test_to_screaming_snake():
    cases = {
        "testCase": "TEST_CASE"
    }
    check_cases(cases, strcase.to_screaming_snake)

def test_to_kebab():
    cases = {
        "testCase": "test-case"
    }
    check_cases(cases, strcase.to_kebab)
    
def test_to_screaming_kebab():
    cases = {
        "testCase": "TEST-CASE"
    }
    check_cases(cases, strcase.to_screaming_kebab)

def test_to_screaming_delimited():
    cases = {
        "testCase": "TEST.CASE"
    }
    check_cases(cases, strcase.to_screaming_delimited, '.')
