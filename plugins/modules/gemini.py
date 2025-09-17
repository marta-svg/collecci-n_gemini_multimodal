from ansible.module_utils.basic import AnsibleModule
from ..module_utils.gemini import Gemini

def main():
    module_args = dict(
        service_account_info = dict(type='dict', required=True),
        project = dict(type='str', required=True),
        location = dict(type='str', required=True),
        model = dict(type='str', required=True, choices=['gemini-1.5-flash', 'gemini-2.0-flash-001', 'gemini-2.0-flash-lite-001']),
        prompt = dict(type='str', required=True),
        context = dict(type='str', required=False, default=""),
        src = dict(type='str', required=False),
        multimodal = dict(type='bool', required=False, default=False),
        multimodal_type = dict(type='str', required=False, choices=['imagen', 'archivo', 'video']),

    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    service_account_info = module.params['service_account_info']
    project = module.params['project']
    location = module.params['location']
    model = module.params['model']
    prompt = module.params['prompt']
    context = module.params['context']
    src = module.params['src']
    multimodal = module.params['multimodal']
    multimodal_type = module.params['multimodal_type']

    run = Gemini( service_account_info, project, location, model, prompt, context, src, multimodal, multimodal_type)
    result = run.call_gemini()
    if result['metadata']['status'] == "failed":
        module.fail_json(msg=result)
    module.exit_json(changed=True, result=result)

if __name__ == '__main__':
    main()  
