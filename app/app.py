import dijo

entry = "! This is a test note for @testproject @test2Project"
print(dijo.create_entry(entry))
dijo.new_entry(dijo.create_entry(entry))