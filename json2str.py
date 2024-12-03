import json

originJson = {
    "config": {
        "enable_forward": True,
        "update_multi": True
    },
    "i18n_elements": {
      "zh_cn": [
        {
          "tag": "column_set",
          "flex_mode": "none",
          "horizontal_spacing": "8px",
          "horizontal_align": "left",
          "columns": [
            {
              "tag": "column",
              "width": "auto",
              "vertical_align": "top",
              "vertical_spacing": "8px",
              "elements": [
                {
                  "tag": "column_set",
                  "flex_mode": "none",
                  "horizontal_spacing": "default",
                  "background_style": "default",
                  "columns": [
                    {
                      "tag": "column",
                      "elements": [
                        {
                          "tag": "div",
                          "text": {
                            "tag": "plain_text",
                            "content": "提问者：",
                            "text_size": "heading",
                            "text_align": "left",
                            "text_color": "default"
                          }
                        }
                      ],
                      "width": "weighted",
                      "weight": 1
                    }
                  ]
                }
              ]
            },
            {
              "tag": "column",
              "width": "weighted",
              "vertical_align": "top",
              "vertical_spacing": "8px",
              "elements": [
                {
                  "tag": "person",
                  "size": "medium",
                  "user_id": "{user_id}"
                }
              ],
              "weight": 1
            }
          ],
          "margin": "16px 0px 0px 0px"
        },
        {
          "tag": "column_set",
          "flex_mode": "none",
          "horizontal_spacing": "default",
          "background_style": "default",
          "columns": [
            {
              "tag": "column",
              "elements": [
                {
                  "tag": "collapsible_panel",
                  "expanded": True,
                  "background_color": "grey",
                  "header": {
                    "title": {
                      "tag": "markdown",
                      "content": "占卜结果"
                    },
                    "vertical_align": "center",
                    "padding": "4px 0px 4px 8px",
                    "icon": {
                      "tag": "standard_icon",
                      "token": "chat-forbidden_outlined",
                      "color": "purple",
                      "img_key": "img_v2_38811724",
                      "size": "16px 16px"
                    },
                    "icon_position": "follow_text",
                    "icon_expanded_angle": -180
                  },
                  "border": {
                    "color": "grey",
                    "corner_radius": "5px"
                  },
                  "vertical_spacing": "8px",
                  "padding": "8px 8px 8px 8px",
                  "elements": [
                    {
                      "tag": "div",
                      "text": {
                        "tag": "plain_text",
                        "content": "{answer}",
                        "text_size": "normal",
                        "text_align": "left",
                        "text_color": "default"
                      }
                    }
                  ]
                }
              ],
              "width": "weighted",
              "weight": 1
            }
          ]
        }
      ]
    },
    "i18n_header": {
      "zh_cn": {
        "title": {
          "tag": "plain_text",
          "content": "{title}"
        },
        "subtitle": {
          "tag": "plain_text",
          "content": ""
        },
        "template": "purple",
        "ud_icon": {
          "tag": "standard_icon",
          "token": "ai-common_colorful"
        }
      }
    }
  }


def escape_json_as_string(json_input):
  """
  将 JSON 转换为转义的字符串。
  :param json_input: dict 或 JSON 格式的字符串
  :return: 转义后的字符串
  """
  if isinstance(json_input, str):
    try:
      # 尝试将 JSON 字符串解析为字典
      json_input = json.loads(json_input)
    except json.JSONDecodeError as e:
      raise ValueError(f"Invalid JSON input: {e}")

  if not isinstance(json_input, dict):
    raise ValueError("Input must be a JSON object or a valid JSON string.")

  # 使用 json.dumps 序列化两次，生成转义的字符串
  return json.dumps(json.dumps(json_input, ensure_ascii=False))

def main():
    # 转换并输出结果
    result = escape_json_as_string(originJson)
    if result:
        print("\n转换后的字符串：")
        print(result)
        # 将结果写入文件
        with open("json2str_output.txt", "w", encoding="utf-8") as f:
            f.write(result)

main()