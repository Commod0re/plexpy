# GetGeoDataGeoData

Geo location data


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The ISO 3166-1 alpha-2 code of the country.                         | VI                                                                  |
| `continent_code`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The continent code where the country is located.                    | NA                                                                  |
| `country`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The official name of the country.                                   | United States Virgin Islands                                        |
| `city`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The name of the city.                                               | Amsterdam                                                           |
| `time_zone`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The time zone of the country.                                       | America/St_Thomas                                                   |
| `postal_code`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The postal code of the location.                                    | 802                                                                 |
| `subdivisions`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The name of the primary administrative subdivision.                 | Saint Thomas                                                        |
| `coordinates`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The geographical coordinates (latitude, longitude) of the location. | 18.3381, -64.8941                                                   |
| `european_union_member`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates if the country is a member of the European Union.         | true                                                                |
| `in_privacy_restricted_country`                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates if the country has privacy restrictions.                  | true                                                                |
| `in_privacy_restricted_region`                                      | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates if the region has privacy restrictions.                   | true                                                                |