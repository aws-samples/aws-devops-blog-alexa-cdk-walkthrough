import { expect as expectCDK, haveResource, haveResourceLike } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as AlexaCdk from '../lib/alexa-cdk-stack';

test('Creates Lambda Function with proper Timeout value and Alexa Skill', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new AlexaCdk.AlexaCdkStack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(haveResourceLike('AWS::Lambda::Function', {
      Timeout: 7
    }));
    expectCDK(stack).to(haveResource('Alexa::ASK::Skill'));
});
