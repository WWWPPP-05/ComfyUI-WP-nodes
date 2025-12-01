"""
ComfyUI-WP-nodes 初始化文件
用于导入和注册自定义节点
"""

# 导入各个节点模块
from .Qwen_镜头预设 import NODE_CLASS_MAPPINGS as lens_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as lens_NODE_DISPLAY_NAME_MAPPINGS
from .Qwen_打光预设 import NODE_CLASS_MAPPINGS as lighting_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as lighting_NODE_DISPLAY_NAME_MAPPINGS
from .Qwen_尺寸预设 import NODE_CLASS_MAPPINGS as size_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as size_NODE_DISPLAY_NAME_MAPPINGS
from .Qwen_泛光效果 import NODE_CLASS_MAPPINGS as bloom_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as bloom_NODE_DISPLAY_NAME_MAPPINGS
from .Qwen_颗粒质感 import NODE_CLASS_MAPPINGS as grain_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as grain_NODE_DISPLAY_NAME_MAPPINGS

# 合并节点映射
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# 合并所有节点类映射
NODE_CLASS_MAPPINGS = merge_dicts(
    lens_NODE_CLASS_MAPPINGS,
    lighting_NODE_CLASS_MAPPINGS,
    size_NODE_CLASS_MAPPINGS,
    bloom_NODE_CLASS_MAPPINGS,
    grain_NODE_CLASS_MAPPINGS
)

# 合并所有节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = merge_dicts(
    lens_NODE_DISPLAY_NAME_MAPPINGS,
    lighting_NODE_DISPLAY_NAME_MAPPINGS,
    size_NODE_DISPLAY_NAME_MAPPINGS,
    bloom_NODE_DISPLAY_NAME_MAPPINGS,
    grain_NODE_DISPLAY_NAME_MAPPINGS
)

# 导出节点映射，供ComfyUI加载使用
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
