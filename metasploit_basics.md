# Modules
- Ruby classes
- Inherit from **Msf::Module**

## Several Types of Modules
### **Exploits**
- Module that uses payload
- exploit without a payload is **Auxillary**

### **Payloads, Encoders, Nops**
- *Payload* code that runs remotely
- *Encoders* ensure payload makes it to destination
- *Nops* keeps payload sizes consistent.

# Payloads
- Created at runtime from components

# Mixins
Ruby's version of composition. Every class has one parrent, but may include
mixins that add and overite methods.

# Plugins
Plugins word directly with the API. Manipulate framework as a whole.
Hook into event subsystem to do events that are tedius manually. 
