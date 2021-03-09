"""
Dictionary containing different AssetTypes and what they are
SOURCE: https://developer.roblox.com/en-us/api-reference/enum/AssetType 
"""

asset_types = {
  1 : "Image",
  2 : "TeeShirt",
  3 : "Audio",
  4 : "Mesh",
  5 : "Lua",
  8 : "Hat",
  9 : "Place",
  10 : "Model",
  11 : "Shirt",	
  12 : "Pants",
  13 : "Decal",
  17 : "Head",
  18 : "Face",
  19 : "Gear",
  21 : "Badge",
  24 : "Animation",
  27 : "Torso",
  28 : "RightArm",
  29 : "LeftArm",	
  30 : "LeftLeg",
  31 : "RightLeg",
  32 : "Package",
  34 : "GamePass",
  38 : "Plugin",
  40 : "MeshPart",	
  41 : "HairAccessory",
  42 : "FaceAccessory",
  43 : "NeckAccessory",
  44 : "ShoulderAccessory",
  45 : "FrontAccessory",
  46 : "BackAccessory",
  47 : "WaistAccessory",
  48 : "ClimbAnimation",
  49 : "DeathAnimation",
  50 : "FallAnimation",
  51 : "IdleAnimation",
  52 : "JumpAnimation",
  53 : "RunAnimation",
  54 : "SwimAnimation",
  55 : "WalkAnimation",
  56 : "PoseAnimation",
  57 : "EarAccessory",
  58 : "EyeAccessory",
  61 : "EmoteAnimation",
  62 : "Video"
}	

"""
URL used to get a user's group data
SOURCE: https://groups.roblox.com/docs#!/Groups/get_v2_users_userId_groups_roles
"""

user_id = 123
group_url = f"https://groups.roblox.com/v2/users/{user_id}/groups/roles"

"""
URL used to get asset data
SOURCE: https://api.roblox.com/docs#Marketplace
"""

asset_id = 123
asset_info_url - f"https://api.roblox.com/Marketplace/ProductInfo?assetId={asset_id}"
