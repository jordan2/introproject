#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#This script will import in unreal all camera in target sequencer
#The script must be used in Unreal Engine Editor with Python plugins : https://docs.unrealengine.com/en-US/Engine/Editor/ScriptingAndAutomation/Python
#Use this command : py "C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\ImportAssetScript.py"


def CheckTasks():
	import unreal
	if hasattr(unreal, 'EditorAssetLibrary') == False:
		print('--------------------------------------------------\n /!\ Warning: Editor Scripting Utilities should be activated.\n Plugin > Scripting > Editor Scripting Utilities.')
		return False
	return True
	
def ImportAllAssets():
	import os.path
	import ConfigParser
	import ast
	import unreal
	
	
	#Prepare var and def
	unrealImportLocation = r'/Game/ImportedFbx'
	ImportedList = []
	ImportFailList = []
	
	def GetOptionByIniFile(FileLoc, OptionName, literal = False):
		Config = ConfigParser.ConfigParser()
		Config.read(FileLoc)
		Options = []
		if Config.has_section(OptionName):
			for option in Config.options(OptionName):
				if (literal == True):
					Options.append(ast.literal_eval(Config.get(OptionName, option)))
				else:
					Options.append(Config.get(OptionName, option))
		else:
			print("/!\ Option: "+OptionName+" not found in file: "+FileLoc)
		return Options
	
	
	#Process import
	print('========================= Import started ! =========================')
	
	
	
	
	'''
	<##############################################################################>
	<#############################	           		#############################>
	<############################	           		 ############################>
	<############################	 StaticMesh tasks	 ############################>
	<############################	           		 ############################>
	<#############################	           		#############################>
	<##############################################################################>
	'''
	
	StaticMesh_TasksList = []
	StaticMesh_PreImportPath = []
	print('========================= Creating StaticMesh tasks... =========================')
	
	def CreateTask_SM_Ground():
		################[ Import Ground as StaticMesh type ]################
		print('================[ New import task : Ground as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_Ground.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_Ground_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : Ground ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "Ground" not found for after inport')
			return
		print('========================= Imports of Ground completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		asset.get_editor_property('asset_import_data').set_editor_property('vertex_color_import_option', unreal.VertexColorImportOption.IGNORE) 
	
		#Import the StaticMesh lod(s)
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			lodTask = unreal.AssetImportTask()
			lodTask.filename = lod
			lodTask.destination_path = AssetImportPath
			lodTask.automated = True
			lodTask.replace_existing = True
			unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([lodTask])
			lodAsset = unreal.find_asset(lodTask.imported_object_paths[0])
			slot_replaced = unreal.EditorStaticMeshLibrary.set_lod_from_static_mesh(asset, x+1, lodAsset, 0, True)
			unreal.EditorAssetLibrary.delete_asset(lodTask.imported_object_paths[0])
		print('========================= Post treatment of Ground completed !	 =========================')
		unreal.EditorAssetLibrary.save_loaded_asset(asset)
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_Ground()
	
	
	
	
	def CreateTask_SM_House():
		################[ Import House as StaticMesh type ]################
		print('================[ New import task : House as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_House.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_House_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : House ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "House" not found for after inport')
			return
		print('========================= Imports of House completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		asset.get_editor_property('asset_import_data').set_editor_property('vertex_color_import_option', unreal.VertexColorImportOption.IGNORE) 
	
		#Import the StaticMesh lod(s)
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			lodTask = unreal.AssetImportTask()
			lodTask.filename = lod
			lodTask.destination_path = AssetImportPath
			lodTask.automated = True
			lodTask.replace_existing = True
			unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([lodTask])
			lodAsset = unreal.find_asset(lodTask.imported_object_paths[0])
			slot_replaced = unreal.EditorStaticMeshLibrary.set_lod_from_static_mesh(asset, x+1, lodAsset, 0, True)
			unreal.EditorAssetLibrary.delete_asset(lodTask.imported_object_paths[0])
		print('========================= Post treatment of House completed !	 =========================')
		unreal.EditorAssetLibrary.save_loaded_asset(asset)
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_House()
	
	
	
	
	def CreateTask_SM_mortar_launcher():
		################[ Import mortar launcher as StaticMesh type ]################
		print('================[ New import task : mortar launcher as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_mortar launcher.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_mortar launcher_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : mortar launcher ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "mortar launcher" not found for after inport')
			return
		print('========================= Imports of mortar launcher completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		asset.get_editor_property('asset_import_data').set_editor_property('vertex_color_import_option', unreal.VertexColorImportOption.IGNORE) 
	
		#Import the StaticMesh lod(s)
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			lodTask = unreal.AssetImportTask()
			lodTask.filename = lod
			lodTask.destination_path = AssetImportPath
			lodTask.automated = True
			lodTask.replace_existing = True
			unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([lodTask])
			lodAsset = unreal.find_asset(lodTask.imported_object_paths[0])
			slot_replaced = unreal.EditorStaticMeshLibrary.set_lod_from_static_mesh(asset, x+1, lodAsset, 0, True)
			unreal.EditorAssetLibrary.delete_asset(lodTask.imported_object_paths[0])
		print('========================= Post treatment of mortar launcher completed !	 =========================')
		unreal.EditorAssetLibrary.save_loaded_asset(asset)
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_mortar_launcher()
	
	
	
	
	def CreateTask_SM_mortar_target():
		################[ Import mortar target as StaticMesh type ]################
		print('================[ New import task : mortar target as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_mortar target.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_mortar target_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : mortar target ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "mortar target" not found for after inport')
			return
		print('========================= Imports of mortar target completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		asset.get_editor_property('asset_import_data').set_editor_property('vertex_color_import_option', unreal.VertexColorImportOption.IGNORE) 
	
		#Import the StaticMesh lod(s)
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			lodTask = unreal.AssetImportTask()
			lodTask.filename = lod
			lodTask.destination_path = AssetImportPath
			lodTask.automated = True
			lodTask.replace_existing = True
			unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([lodTask])
			lodAsset = unreal.find_asset(lodTask.imported_object_paths[0])
			slot_replaced = unreal.EditorStaticMeshLibrary.set_lod_from_static_mesh(asset, x+1, lodAsset, 0, True)
			unreal.EditorAssetLibrary.delete_asset(lodTask.imported_object_paths[0])
		print('========================= Post treatment of mortar target completed !	 =========================')
		unreal.EditorAssetLibrary.save_loaded_asset(asset)
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_mortar_target()
	
	
	
	
	def CreateTask_SM_Grimbler():
		################[ Import Grimbler as StaticMesh type ]################
		print('================[ New import task : Grimbler as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_Grimbler.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_Grimbler_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : Grimbler ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "Grimbler" not found for after inport')
			return
		print('========================= Imports of Grimbler completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		asset.get_editor_property('asset_import_data').set_editor_property('vertex_color_import_option', unreal.VertexColorImportOption.IGNORE) 
	
		#Import the StaticMesh lod(s)
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			lodTask = unreal.AssetImportTask()
			lodTask.filename = lod
			lodTask.destination_path = AssetImportPath
			lodTask.automated = True
			lodTask.replace_existing = True
			unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([lodTask])
			lodAsset = unreal.find_asset(lodTask.imported_object_paths[0])
			slot_replaced = unreal.EditorStaticMeshLibrary.set_lod_from_static_mesh(asset, x+1, lodAsset, 0, True)
			unreal.EditorAssetLibrary.delete_asset(lodTask.imported_object_paths[0])
		print('========================= Post treatment of Grimbler completed !	 =========================')
		unreal.EditorAssetLibrary.save_loaded_asset(asset)
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_Grimbler()
	
	
	
	
	def CreateTask_SM_mortar_shell():
		################[ Import mortar shell as StaticMesh type ]################
		print('================[ New import task : mortar shell as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_mortar shell.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\heide\Documents\Unreal Projects\introproject\Content\Blender Imports\ExportedFbx\StaticMesh\SM_mortar shell_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = unreal.AssetImportTask()
		task.filename = FilePath
		task.destination_path = AssetImportPath
		task.automated = True
		task.save = True
		task.replace_existing = True
		task.set_editor_property('options', unreal.FbxImportUI())
		task.get_editor_property('options').set_editor_property('original_import_type', unreal.FBXImportType.FBXIT_STATIC_MESH)
		task.get_editor_property('options').set_editor_property('import_materials', True)
		task.get_editor_property('options').set_editor_property('import_textures', False)
		task.get_editor_property('options').set_editor_property('import_animations', False)
		task.get_editor_property('options').set_editor_property('import_mesh', True)
		task.get_editor_property('options').set_editor_property('create_physics_asset', True)
		task.get_editor_property('options').texture_import_data.set_editor_property('material_search_location', unreal.MaterialSearchLocation.LOCAL)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('combine_meshes', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('auto_generate_collision', True)
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('static_mesh_lod_group', 'None')
		task.get_editor_property('options').static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
		print('================[ import asset : mortar shell ]================')
		unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
		asset = unreal.find_asset(task.imported_object_paths[0])
		if asset == None:
			ImportFailList.append('Asset "mortar shell" not found for after inport')
			return
		print('========================= Imports of mortar shell completed ! Post treatment started...	=========================')
		asset.set_editor_property('lod_group', 'None')
		asset.get_editor_property('body_setup').set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_DEFAULT) 
		asset.get_editor_property('asset_import_data').set_editor_property('vertex_color_import_option', unreal.VertexColorImportOption.IGNORE) 
	
		#Import the StaticMesh lod(s)
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			lodTask = unreal.AssetImportTask()
			lodTask.filename = lod
			lodTask.destination_path = AssetImportPath
			lodTask.automated = True
			lodTask.replace_existing = True
			unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([lodTask])
			lodAsset = unreal.find_asset(lodTask.imported_object_paths[0])
			slot_replaced = unreal.EditorStaticMeshLibrary.set_lod_from_static_mesh(asset, x+1, lodAsset, 0, True)
			unreal.EditorAssetLibrary.delete_asset(lodTask.imported_object_paths[0])
		print('========================= Post treatment of mortar shell completed !	 =========================')
		unreal.EditorAssetLibrary.save_loaded_asset(asset)
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_mortar_shell()
	
	
	
	
	print('========================= Full import completed !  =========================')
	
	StaticMesh_ImportedList = []
	SkeletalMesh_ImportedList = []
	Alembic_ImportedList = []
	Animation_ImportedList = []
	for asset in ImportedList:
		if asset[1] == 'StaticMesh':
			StaticMesh_ImportedList.append(asset[0])
		elif asset[1] == 'SkeletalMesh':
			SkeletalMesh_ImportedList.append(asset[0])
		elif asset[1] == 'Alembic':
			Alembic_ImportedList.append(asset[0])
		else:
			Animation_ImportedList.append(asset[0])
	
	print('Imported StaticMesh: '+str(len(StaticMesh_ImportedList)))
	print('Imported SkeletalMesh: '+str(len(SkeletalMesh_ImportedList)))
	print('Imported Alembic: '+str(len(Alembic_ImportedList)))
	print('Imported Animation: '+str(len(Animation_ImportedList)))
	print('Import failled: '+str(len(ImportFailList)))
	for error in ImportFailList:
		print(error)
	
	#Select asset(s) in content browser
	PathList = []
	for asset in (StaticMesh_ImportedList + SkeletalMesh_ImportedList + Alembic_ImportedList + Animation_ImportedList):
		PathList.append(asset.get_path_name())
	unreal.EditorAssetLibrary.sync_browser_to_objects(PathList)
	
	print('=========================')
	if len(ImportFailList) == 0:
		return 'Assets imported with success !' 
	else:
		return 'Some asset(s) could not be imported.' 
	
if CheckTasks() == True:
	print(ImportAllAssets())
