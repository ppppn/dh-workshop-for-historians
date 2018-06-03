# API Reference for Hyakunin-Isshu Search

## GET song/<id>

Returns a single Hyakunin-Isshu Song, specified by the `id` parameter.
The writer will also be embedded within the Song.

#### About Writer's Title

If the writer has no title, then there will be an empty `writer_title`.

### Resource URL

`http://localhost:10080/song/<id>`

### Resource Information

| Key                      | Value                                                 |
|--------------------------|-------------------------------------------------------|
| Response formats         | Original format (values in 1 line, separated by `|`   |
| Requires authentication? | No                                                    |
| Rate limited?            | No                                                    |

### Parameters

| Name | Required | Description                                                 | Default Value | Example |
|------|----------|-------------------------------------------------------------|---------------|---------|
| id   | required | The numerical ID of the desired Song. It must be in 1 - 100 | None          | 10      |

### Example Request

`GET http://localhost:10080/song/1`

### Example Response

```
1|天智天皇||秋の田の　かりほの庵の　苫をあらみ|わが衣手は　露にぬれつつ
```

### See Also

https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-show-id
http://parliament-api-docs.readthedocs.io/en/latest/new-south-wales/