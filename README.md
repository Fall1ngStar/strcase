# strcase

strcase is a python package for converting string case.

It is a port of the go package [strcase](https://github.com/iancoleman/strcase)

## Example

```python
s = "AnyKind of_string"
```

| Function                          | Result               |
|-----------------------------------|----------------------|
| `to_snake(s)`                      | `any_kind_of_string` |
| `to_screaming_snake(s)`             | `ANY_KIND_OF_STRING` |
| `to_kebab(s)`                      | `any-kind-of-string` |
| `to_screaming_kebab(s)`             | `ANY-KIND-OF-STRING` |
| `to_delimited(s, '.')`             | `any.kind.of.string` |
| `to_screaming_delimited(s, '.')`    | `ANY.KIND.OF.STRING` |
| `to_camel(s)`                      | `AnyKindOfString`    |
| `to_lower_camel(s)`                 | `anyKindOfString`    |