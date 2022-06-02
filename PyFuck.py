# Minimum Turing completeness charset: exc('%0)
from Compile import compile_bce0, compile_b_comma, compile_final


encoded, args = compile_bce0("""print('hello')""", "exc(%0)b,")
encoded = f"""exec("{encoded}"%{args})"""
print(encoded)

encoded, args = compile_b_comma(encoded)
encoded = f"""exec('{encoded}'%{args})"""
print(encoded)

encoded, args = compile_bce0(encoded)
encoded = f"""exec("{encoded}"%{args})"""
print(encoded)

encoded, args = compile_final(encoded)
encoded = f"""exec('''{encoded}'''{args})"""
print(encoded)
print("compiled length:", len(encoded), sep="\t\t")
print("charset and length:", ''.join(sorted(set(encoded))), len(set(encoded)), sep="\t\t")


encoded, args = compile_bce0("""print('hello')""", list("exc('%0)")+[chr(c) for c in range(0, 128, 2)])
encoded = f"""exec("{encoded}"%{args})"""
print(encoded)

encoded, args = compile_final(encoded)
encoded = f"""exec('''{encoded}'''{args})"""
print(encoded)
print("compiled length:", len(encoded), sep="\t\t")
print("charset and length:", ''.join(sorted(set(encoded))), len(set(encoded)), sep="\t\t")
