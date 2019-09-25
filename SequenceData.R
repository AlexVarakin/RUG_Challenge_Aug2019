#Extract Daya for challenege, save to csv file so I can open it in Python!

Sequence <- 
  structure(list(sequence_id = c("87d28a20-cb8f-4aac-a3ec-c11931ea4700", 
                                 "18b4a490-e903-4172-a794-f829a3416526", "e834936f-6f49-4d84-a3da-bf8640dfaa18", 
                                 "076b7778-5922-42cb-a185-035deeb9e3a0", "5020dc7f-97a6-4276-8ce8-a2d0818cf562", 
                                 "cf0f96f8-a0dd-44e9-a15d-993b7d5c1834", "e412f327-3479-4bd1-8975-7bc9c7a12042", 
                                 "b0454b64-1995-4d05-8687-4164b956dda1", "d0cddbc7-4d32-488a-8952-1e5dd8b0c9e8", 
                                 "f38ce43a-2203-4e49-b25e-aa9872c256ea", "5b075845-2503-470c-9127-577ba8bf7ab0", 
                                 "a2133ee7-2054-401c-bae5-8c48c68c3e37", "9405e5cf-dee0-4f5d-a5b9-ae076f31b5c8", 
                                 "136c6673-7256-487f-880b-f80cb399e28c"), timestamp = c(636583527529040640, 
                                                                                        636583532508248704, 636583620119675264, 636583629461627392, 636583639616867456, 
                                                                                        636583666169027584, 636583749734024064, 636583833493856640, 636583917036381184, 
                                                                                        636584000270025728, 636584333029101824, 636584368212426112, 636585295224467968, 
                                                                                        636585307253700096), first_analysis = structure(c(1522770608, 
                                                                                                                                          1522771047, 1522779884, 1522780766, 1522781775, 1522784437, 1522792887, 
                                                                                                                                          1522801254, 1522809610, 1522817937, 1522851194, 1522854764, 1522947339, 
                                                                                                                                          1522948536), class = c("POSIXct", "POSIXt"), tzone = "")), class = "data.frame", row.names = c(NA, 
                                                                                                                                                                                                                                         -14L), .Names = c("sequence_id", "timestamp", "first_analysis"
                                                                                                                                                                                                                                         ))

write.csv(Sequence,"~/Documents/Documents/RUG/RUGChallene1.csv")



