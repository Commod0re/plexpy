# CreatePlaylistRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `title`                                              | *str*                                                | :heavy_check_mark:                                   | name of the playlist                                 |
| `type`                                               | [operations.Type](../../models/operations/type.md)   | :heavy_check_mark:                                   | type of playlist to create                           |
| `smart`                                              | [operations.Smart](../../models/operations/smart.md) | :heavy_check_mark:                                   | whether the playlist is smart or not                 |
| `uri`                                                | *Optional[str]*                                      | :heavy_minus_sign:                                   | the content URI for the playlist                     |
| `play_queue_id`                                      | *Optional[float]*                                    | :heavy_minus_sign:                                   | the play queue to copy to a playlist                 |