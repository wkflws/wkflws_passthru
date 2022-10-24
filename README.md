# wkflws_passthru
This node provides a simple HTTP request passthrough.

## wkflws_passthru.triggers.passthru

This node will accept any HTTP request (including non-JSON but it really should be JSON) and provide it to the next node unmodified. This can be useful for testing or quick proof-of-concept workflows where a custom trigger node doesn't exist.
